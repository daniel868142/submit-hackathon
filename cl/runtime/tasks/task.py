# Copyright (C) 2023-present The Project Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime as dt
import time
from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from typing_extensions import Self
from cl.runtime.context.context import Context
from cl.runtime.log.exceptions.user_error import UserError
from cl.runtime.log.log_message import LogMessage
from cl.runtime.primitive.datetime_util import DatetimeUtil
from cl.runtime.primitive.timestamp import Timestamp
from cl.runtime.records.dataclasses_extensions import missing
from cl.runtime.records.record_mixin import RecordMixin
from cl.runtime.tasks.task_key import TaskKey
from cl.runtime.tasks.task_queue_key import TaskQueueKey
from cl.runtime.tasks.task_status_enum import TaskStatusEnum


@dataclass(slots=True, kw_only=True)
class Task(TaskKey, RecordMixin[TaskKey], ABC):
    """
    The task 'run_task' method is invoked by the queue to which the task is submitted.

    Notes:
        - The task may run sequentially or in parallel with other tasks
        - The task may run in a different process, thread or machine than the submitting code
          and must be able to acquire the resources required by its 'run_task' method in all of these cases
        - The queue updates 'status' field of the task as it progresses from its initial Pending state through
          the Running and optionally Paused state and ending in one of Completed, Failed, or Cancelled states
    """

    label: str | None = None  # TODO: Make required
    """Label for information purposes only (should not be used in processing)."""

    queue: TaskQueueKey = missing()
    """The queue that will run the task once it is saved."""

    status: TaskStatusEnum = missing()
    """Begins from Pending, continues to Running or Paused, and ends with Completed, Failed, or Cancelled."""

    progress_pct: float = missing()
    """Task progress in percent from 0 to 100."""

    elapsed_sec: float | None = None
    """Elapsed time in seconds if available."""

    remaining_sec: float | None = None
    """Remaining time in seconds if available."""

    error_message: str | None = None
    """Error message for Failed status if available."""

    def get_key(self) -> TaskKey:
        return TaskKey(task_id=self.task_id)

    def init(self) -> Self:
        # Set or validate task_id
        if self.task_id is None:
            # Automatically generate time-ordered unique task run identifier in UUIDv7 format if not specified
            self.task_id = Timestamp.create()
        else:
            # Otherwise validate
            Timestamp.validate(self.task_id, value_name="task_id", data_type="TaskKey")

        # Set status and progress_pct if not yet set
        if self.status is None:
            self.status = TaskStatusEnum.PENDING
        if self.progress_pct is None:
            self.progress_pct = 0.0

        # Return self to enable method chaining
        return self

    @abstractmethod
    def _execute(self) -> None:
        """Run payload without updating status or handling exceptions (protected, callers should invoke 'run_task')."""

    def run_task(self) -> None:
        """Invoke execute with task status updates and exception handling."""
        # Record the start time
        start_time = DatetimeUtil.now()

        context = Context.current()
        try:
            # Set status to Running and save
            self.status = TaskStatusEnum.RUNNING
            context.save_one(self)

            # Run the payload
            self._execute()

        except Exception as e:  # noqa

            # TODO: Perform additional processing for UserError
            if isinstance(e, UserError):
                # TODO: Perform additional processing
                pass
            else:
                # TODO: Perform additional processing
                pass

            # Create log entry
            log_message = LogMessage(message=str(e))
            log_message.init()

            # Save log entry to the database
            Context.current().save_one(log_message)

            # Update task run record to report task failure
            self.status = TaskStatusEnum.FAILED
            self.progress_pct = 100.0
            self.elapsed_sec = 0.0  # TODO: Implement
            self.remaining_sec = 0.0
            self.error_message = str(e)
            context.save_one(self)
        else:
            # Record the end time
            end_time = DatetimeUtil.now()

            # Update task run record to report task completion
            self.status = TaskStatusEnum.COMPLETED
            self.progress_pct = 100.0
            self.elapsed_sec = 0.0  # TODO: Implement
            self.remaining_sec = 0.0
            context.save_one(self)

    @classmethod
    def wait_for_completion(cls, task_key: TaskKey, timeout_sec: int = 10) -> None:  # TODO: Rename or move
        """Wait for completion of the specified task run before exiting from this method (not async/await)."""

        context = Context.current()
        start_datetime = DatetimeUtil.now()
        while DatetimeUtil.now() < start_datetime + dt.timedelta(seconds=timeout_sec):
            task = context.load_one(Task, task_key)
            if task.status == TaskStatusEnum.COMPLETED:
                # Test success, task has been completed
                return
            # TODO: Refactor to use queue-specific push communication rather than heartbeat
            time.sleep(1)  # Sleep for 1 second to reduce CPU load

        # Test failure
        raise RuntimeError(f"Task has not been completed after {timeout_sec} sec.")
