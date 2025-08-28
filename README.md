# Vanguard A/B Test – Online Process UX

**Goal**  
Evaluate whether the new, more intuitive UI with in‑context prompts improves client completion rate versus the current control experience.

## Dataset(s)
- **Demo**: df_final_demo.csv  
- **Web (parts 1–2)**: df_final_web_data_pt_1.csv, df_final_web_data_pt_2.csv  
- **Experiment clients**: df_final_experiment_clients.csv  
> Place raw files in `data/raw/` and any cleaned/merged outputs in `data/processed/`.

## Key DataFrames (DF)
- `df_demo` – demographic features.  
- `df_web_complete` – merged web data (parts 1–2).  
- `df_core` – consolidated table with `variation` (Control/Test), `process_step_code`, completion/error flags.  
- `df_experiment_clients` – participants in experiment.
> Update names if your notebook uses different ones.

## KPIs
- **Completion Rate** = completed / total users.  
- **Error Rate** = error events / total users (or per session, define consistently).  
- Grouped by **variation** (Control vs Test).

## Statistical Test
- **Chi‑square test of independence** on a 2×2 table (Completed vs Not Completed × Test vs Control).  
- Report: χ², p‑value, dof, effect size (φ or Cramér’s V).

## Repo Structure
```
Vanguard-abtest/
├─ README.md
├─ DELIVERABLES.md
├─ requirements.txt
├─ .gitignore
├─ src/
│  └─ functions.py
├─ notebooks/
│  └─ 01_eda_baseline5.ipynb   # <- Final notebook (add your file here)
├─ data/
│  ├─ raw/
│  └─ processed/
└─ figures/
```
> Keep the notebook path/name as above so teammates/instructors can find it quickly.

## How to Run
1. Create and activate a virtual environment (optional).
2. Install deps: `pip install -r requirements.txt`  
3. Open the notebook in `notebooks/` and run all cells.  
4. If using `src/functions.py`, import with:
```python
from src.functions import (csv_mini_clean, build_contingency_table,
                           chi_square_test, compute_rates)
```

## Slides
Add your Google Slides link here (View‑only):  
- [Slides](https://docs.google.com/presentation/d/11uPlTww5BHim5_AVdJEL_pZpJgZu_85GQPbEIvphxGM/edit?usp=sharing)

## Results (to summarize after final run)
- Completion rate: Control __ vs Test __  
- Error rate: Control __ vs Test __  
- Chi‑square: χ²=__, p=__, effect size φ=__  
- Short takeaway: __

## Authors
Team: Lalo & Pedro – Ironhack Data Analytics (Module 2)
