# This file makes the src directory a Python package.


#Not sure anyhting else should be in here, but here is what CoPilot said. CahtGPT and Gemini both said not to include this.



# src/__init__.py
# Package initializer: re-export commonly used functions for convenience.

from .io_utils import ensure_dirs, read_data
from .profiling import basic_profile, split_columns
from .summaries import (
    summarize_numeric,
    summarize_categorical,
    correlations,
    missingness_table,
)
from .modeling import multiple_linear_regression
from .plotting import (
    plot_missingness,
    plot_corr_heatmap,
    plot_histograms,
    plot_bar_charts,
)
from .checks import assert_json_safe, target_check

__all__ = [
    "ensure_dirs",
    "read_data",
    "basic_profile",
    "split_columns",
    "summarize_numeric",
    "summarize_categorical",
    "correlations",
    "missingness_table",
    "multiple_linear_regression",
    "plot_missingness",
    "plot_corr_heatmap",
    "plot_histograms",
    "plot_bar_charts",
    "assert_json_safe",
    "target_check",
]

