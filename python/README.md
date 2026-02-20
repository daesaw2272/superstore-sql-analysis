python

This folder contains Python scripts used to generate visualisations from SQL-derived CSV files.

Purpose
Python is used to:
- Load aggregated CSV outputs from SQL
- Generate charts to visualise trends and performance
- Save figures for inclusion in documentation and reporting

Files
- `plots.py`  
  Reads CSV files from the `/exports` folder and generates:
  - Profit by region bar chart
  - Monthly sales trend line chart
  - Monthly profit trend line chart
  - Bottom 10 loss-making sub-categories
  - Top 10 customers by profit

Requirements
Dependencies are listed in the root `requirements.txt` file:
- pandas
- matplotlib

How to Run
From the repository root:

```bash
pip install -r requirements.txt
python python/plots.py
