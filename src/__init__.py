# This file makes the src directory a Python package.


#Not sure anyhting else should be in here, but here is what CoPilot said. CahtGPT and Gemini both said not to include this.



# src/__init__.py
# Package initializer: re-export commonly used functions for convenience.
"""Create "src" package with reusable functions to serve as tools for future agent builds."""

from .io_utils import ensure_dirs, read_data
from .profiling import basic_profile, split_columns
from .summaries import (
    summarize_numeric,
    summarize_categorical,
    correlations,
    missingness_table,
    pearson_correlation,
)
from .modeling import multiple_linear_regression
from .plotting import (
    plot_missingness,
    plot_corr_heatmap,
    plot_histograms,
    plot_bar_charts,
    plot_cat_num_boxplot,
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
    "pearson_correlation",
    "plot_missingness",
    "plot_corr_heatmap",
    "plot_histograms",
    "plot_bar_charts",
    "plot_cat_num_boxplot",
    "assert_json_safe",
    "target_check",
]

