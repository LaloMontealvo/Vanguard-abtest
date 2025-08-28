# src/functions.py
# Utility functions for Vanguard A/B Test project.
# Keep the APIs minimal and readable for the bootcamp rubric.

from typing import Tuple
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
# Optional plotting (used in notebooks)
import matplotlib.pyplot as plt

def csv_mini_clean(df: pd.DataFrame,
                   datetime_cols=None,
                   numeric_cols=None,
                   dropna_subset=None) -> pd.DataFrame:
    """Minimal, non‑aggressive CSV cleaning.
    - strip text cols
    - opt‑in parse dates & numeric with errors='coerce'
    - drop_duplicates
    - optional dropna on subset
    """
    df = df.copy()
    # Strip text columns
    for c in df.select_dtypes(include=["object"]).columns:
        df[c] = df[c].astype(str).str.strip()
    # Parse dates
    if datetime_cols:
        for c in datetime_cols:
            df[c] = pd.to_datetime(df[c], errors="coerce")
    # Parse numeric
    if numeric_cols:
        for c in numeric_cols:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    # Duplicates
    df = df.drop_duplicates()
    # Optional NA drop
    if dropna_subset:
        df = df.dropna(subset=dropna_subset)
    return df

def compute_rates(df: pd.DataFrame,
                  group_col: str = "variation",
                  completed_col: str = "completed",
                  error_col: str = "error_flag") -> pd.DataFrame:
    """Return completion and error rates by group_col."""
    g = df.groupby(group_col).agg(
        completed_sum=(completed_col, "sum"),
        completed_total=(completed_col, "count"),
        error_sum=(error_col, "sum")
    )
    g["completion_rate"] = g["completed_sum"] / g["completed_total"].replace(0, np.nan)
    g["error_rate"] = g["error_sum"] / g["completed_total"].replace(0, np.nan)
    return g.reset_index()

def build_contingency_table(df: pd.DataFrame,
                            group_col: str = "variation",
                            completed_col: str = "completed") -> pd.DataFrame:
    """2×2 Completed vs Not Completed by group (Control/Test)."""
    comp = pd.crosstab(df[group_col], df[completed_col])
    # Ensure both 0 and 1 columns exist
    for col in [0,1]:
        if col not in comp.columns:
            comp[col] = 0
    comp = comp[[0,1]]  # order: not completed, completed
    return comp

def chi_square_test(table: pd.DataFrame) -> Tuple[float, float, int, np.ndarray]:
    """Run chi‑square test of independence on a contingency table."""
    chi2, p, dof, expected = chi2_contingency(table.values)
    return chi2, p, dof, expected

def plot_rates(rates_df: pd.DataFrame,
               group_col: str = "variation") -> None:
    """Simple bar plots for completion and error rates."""
    ax = rates_df.plot(x=group_col, y="completion_rate", kind="bar")
    ax.set_ylabel("Completion rate")
    plt.show()
    ax2 = rates_df.plot(x=group_col, y="error_rate", kind="bar")
    ax2.set_ylabel("Error rate")
    plt.show()
