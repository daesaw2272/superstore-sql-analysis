SELECT
  ROUND(SUM(sales), 2)  AS total_sales,
  ROUND(SUM(profit), 2) AS total_profit,
  ROUND(100.0 * SUM(profit) / NULLIF(SUM(sales), 0), 2) AS profit_margin_pct
FROM public.superstore;

SELECT
  region,
  ROUND(SUM(sales), 2)  AS sales,
  ROUND(SUM(profit), 2) AS profit
FROM public.superstore
GROUP BY region
ORDER BY profit DESC;

SELECT
  category,
  sub_category,
  ROUND(SUM(sales), 2)  AS sales,
  ROUND(SUM(profit), 2) AS profit
FROM public.superstore
GROUP BY category, sub_category
ORDER BY profit ASC;

SELECT
  DATE_TRUNC('month', order_date) AS month,
  ROUND(SUM(sales), 2)  AS sales,
  ROUND(SUM(profit), 2) AS profit
FROM public.superstore
GROUP BY month
ORDER BY month;

WITH product_profit AS (
  SELECT
    region,
    product_name,
    SUM(profit) AS profit
  FROM public.superstore
  GROUP BY region, product_name
),
ranked AS (
  SELECT
    region,
    product_name,
    profit,
    DENSE_RANK() OVER (PARTITION BY region ORDER BY profit DESC) AS rnk
  FROM product_profit
)
SELECT
  region,
  product_name,
  ROUND(profit, 2) AS profit
FROM ranked
WHERE rnk <= 3
ORDER BY region, profit DESC;
