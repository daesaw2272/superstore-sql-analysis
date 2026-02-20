SELECT COUNT(*) FROM public.superstore;SELECT COUNT(*) FROM public.superstore;

ALTER TABLE public.superstore
ALTER COLUMN order_date TYPE DATE
USING TO_DATE(order_date, 'MM/DD/YYYY');

ALTER TABLE public.superstore
ALTER COLUMN ship_date TYPE DATE
USING TO_DATE(ship_date, 'MM/DD/YYYY');


SELECT
    MIN(order_date),
    MAX(order_date),
    MIN(ship_date),
    MAX(ship_date)
FROM public.superstore;