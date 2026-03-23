from __future__ import annotations
from pathlib import Path
import pandas as pd

def ensure_dirs(reports: Path) -> None:
    """Create output folders."""
    # BLANK 1: create the figures folder
    # HINT: (reports / "figures").mkdir(...)
    (reports / "figures").mkdir(parents=True, exist_ok=True) #Blank 1


def read_data(path: Path) -> pd.DataFrame:
    """Read a CSV file into a DataFrame with basic error handling."""
    # BLANK 2: raise FileNotFoundError if path does not exist
    if not path.exists(): #Blank 2
        raise FileNotFoundError

    # BLANK 3: read the CSV into df
    df = pd.read_csv(path) #Blank 3

    if df.empty:
        raise ValueError("Loaded dataframe is empty.")
    return df



"""
from pathlib import Path
from typing import Optional

import pandas as pd


def ensure_dirs(reports: Path) -> None:
    # BLANK 1: create the figures folder
    # HINT: (reports / "figures").mkdir(...)
    (reports / "figures").mkdir(parents=True, exist_ok=True) #Blank 1


def read_data(path: Path) -> pd.DataFrame:
    # BLANK 2: raise FileNotFoundError if path does not exist
    if not path.exists(): #Blank 2
        raise FileNotFoundError

    # BLANK 3: read the CSV into df
    df = pd.read_csv(path) #Blank 3

    if df.empty:
        raise ValueError("Loaded dataframe is empty.")
    return df

"""
