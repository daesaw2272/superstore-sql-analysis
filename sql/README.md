sql

This folder contains all SQL scripts used in the Superstore Sales Analysis project.

Purpose
The SQL scripts are responsible for:
- Defining the database schema
- Cleaning and transforming raw data
- Performing analytical queries to derive business insights

Contents
- `01_create_table.sql`  
  Creates the `superstore` table with appropriate data types.

- `02_clean_dates.sql`  
  Ensures date fields (`order_date`, `ship_date`) are stored and parsed correctly.

- `03_analysis.sql`  
  Core analytical queries including:
  - Total sales, profit, and margin
  - Regional performance
  - Loss-making product categories
  - Monthly sales and profit trends
  - Ranking top customers and products by profitability

Notes
These scripts are database-agnostic but were developed and tested using PostgreSQL.
