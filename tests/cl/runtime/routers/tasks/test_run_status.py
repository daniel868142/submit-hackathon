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

import pytest
from typing import Dict
from typing import List
from fastapi import FastAPI
from starlette.testclient import TestClient
from cl.runtime import Context
from cl.runtime.context.testing_context import TestingContext
from cl.runtime.routers.tasks import tasks_router
from cl.runtime.routers.tasks.run_response_item import handler_queue
from cl.runtime.routers.tasks.task_status_request import TaskStatusRequest
from cl.runtime.routers.tasks.task_status_response_item import TaskStatusResponseItem
from cl.runtime.tasks.instance_method_task import InstanceMethodTask
from stubs.cl.runtime import StubHandlers
from stubs.cl.runtime.records.for_dataclasses.stub_dataclass_handlers_key import StubHandlersKey


def _save_tasks_and_get_requests() -> List[Dict]:
    """Creates and saves tasks."""

    # Create handler tasks
    queue_key = handler_queue.get_key()
    tasks = [
        InstanceMethodTask.create(
            queue=queue_key,
            record_or_key=StubHandlersKey(stub_id=f"{i}"),
            method_callable=StubHandlers.run_instance_method_1a,
        )
        for i in range(2)
    ]
    Context.current().save_many(tasks)

    requests = [
        {
            "task_run_ids": [str(task.task_id) for task in tasks],
            "db": "DEPRECATED",
            "dataset": "",
        }
    ]
    return requests


def test_method():
    """Test coroutine for /tasks/run/status route."""

    with TestingContext() as context:

        for request in _save_tasks_and_get_requests():
            request_obj = TaskStatusRequest(**request)
            result = TaskStatusResponseItem.get_task_statuses(request_obj)

            assert isinstance(result, list)
            for result_response_item, task_run_id in zip(result, request_obj.task_run_ids):

                # Validate type
                assert isinstance(result_response_item, TaskStatusResponseItem)

                # Validate fields
                # TODO: Review the spec for the value of result_response_item.key
                assert isinstance(result_response_item.key, str)
                assert result_response_item.task_run_id == task_run_id
                assert result_response_item.status_code is not None


def test_api():
    """Test REST API for /tasks/run/status route."""

    # TODO: Use TestingContext instead
    with TestingContext():

        test_app = FastAPI()
        test_app.include_router(tasks_router.router, prefix="/tasks", tags=["Tasks"])
        with TestClient(test_app) as test_client:
            for request in _save_tasks_and_get_requests():

                # Invoke
                response = test_client.post("/tasks/run/status", json=request)
                assert response.status_code == 200
                result = response.json()

                # Validate
                assert isinstance(result, list)
                request_obj = TaskStatusRequest(**request)
                for result_item, task_run_id in zip(result, request_obj.task_run_ids):

                    # Validate with Pydantic
                    result_response_item = TaskStatusResponseItem(**result_item)

                    # Validate fields
                    # TODO: Review the spec for the value of result_response_item.key
                    assert isinstance(result_response_item.key, str)
                    assert result_response_item.task_run_id == task_run_id
                    assert result_response_item.status_code is not None


if __name__ == "__main__":
    pytest.main([__file__])