Exported CSV Files

This folder contains CSV files exported from PostgreSQL query results.

Purpose
These files represent **aggregated, analysis-ready datasets** derived from SQL queries.
They are used as inputs for Python-based visualisations and reporting.

Files Included
- `kpis_overall.csv`  
  Overall business KPIs including total sales, total profit, and profit margin.

- `region_performance.csv`  
  Sales and profit aggregated by region.

- `monthly_trend.csv`  
  Monthly sales and profit time series.

- `subcategory_profit.csv`  
  Sales and profit by product category and sub-category.

- `top_customers_profit.csv`  
  Top 10 customers ranked by total profit.

- `top_products_by_region.csv`  
  Top-performing products by profit within each region.

Notes
These CSVs were exported directly from SQL query results to ensure reproducibility.
The original transactional dataset is not modified manually.
