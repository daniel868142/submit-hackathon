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

from dataclasses import dataclass
from pathlib import Path
import pandas as pd
from cl.runtime import Context
from cl.runtime.plots.confusion_matrix_plot import ConfusionMatrixPlot
from cl.runtime.views.plot_view import PlotView
from stubs.cl.runtime.views.stub_viewers import StubViewers


@dataclass(slots=True, kw_only=True)
class StubPlotViewers(StubViewers):
    """Class with plot viewers."""

    @classmethod
    def _create_confusion_matrix_plot(cls):
        """Create confusion matrix plot from data in csv."""
        raw_data = pd.read_csv(Path(__file__).resolve().parent / "./stub_plot_viewers_confusion_matrix.csv")

        matrix_plot = ConfusionMatrixPlot()
        matrix_plot.title = "Confusion Matrix"
        matrix_plot.expected_categories = raw_data["True Category"].values.tolist()
        matrix_plot.received_categories = raw_data["Predicted"].values.tolist()
        return matrix_plot

    def view_confusion_matrix_plot_png(self):
        """Png viewer for MatplotlibPlot with theme."""

        # Create ConfusionMatrixPlot instance
        matrix_plot = self._create_confusion_matrix_plot()

        # Return PngView
        return matrix_plot.get_view()

    def view_confusion_matrix_plot_with_record(self):
        """Plot viewer for MatplotlibPlot as record with theme."""

        # Create ConfusionMatrixPlot instance
        matrix_plot = self._create_confusion_matrix_plot()

        # Return PlotView
        return PlotView(plot=matrix_plot)

    def view_confusion_matrix_plot_with_key(self):
        """Plot viewer for MatplotlibPlot as key with theme."""

        # Create ConfusionMatrixPlot instance
        matrix_plot = self._create_confusion_matrix_plot()
        matrix_plot.plot_id = "confusion_matrix_plot"

        Context.current().save_one(matrix_plot)

        # Return PlotView
        return PlotView(plot=matrix_plot.get_key())
