--------------------------------------------------------
-- Task 1 -- Countries that are operated in and number of stores --
SELECT 
    country_code, 
    COUNT(*) as total_no_stores
FROM 
    dim_store_details
GROUP BY 
    country_code
ORDER BY 
    total_no_stores DESC;
--Recieves an extra store for GB--

--------------------------------------------------------
-- Task 2 -- Number of stores in each location --
SELECT 
    locality, 
    COUNT(*) as total_no_stores
FROM 
    dim_store_details
GROUP BY 
    locality
ORDER BY 
    total_no_stores DESC
LIMIT
    7;

--------------------------------------------------------
-- Task 3 -- Total sales of each month --
SELECT 
    dim_date_times.month, SUM(orders_table.product_quantity * dim_products.product_price) as total_sales
FROM 
    orders_table
JOIN 
    dim_date_times ON orders_table.date_uuid = dim_date_times.date_uuid
JOIN 
    dim_products ON orders_table.product_code = dim_products.product_code
GROUP BY 
    dim_date_times.month
ORDER BY 
    total_sales DESC;

--------------------------------------------------------
-- Task 4 -- Number of sales from web orders and offline --
SELECT * FROM orders_table
SELECT * FROM dim_store_details

SELECT 
    COUNT(product_quantity) AS number_of_sales,
    SUM(product_quantity) AS product_quantity_count,
    CASE
        WHEN dim_store_details.store_type = 'Web Portal' THEN 'Web'
        ELSE 'Offline'
    END AS location
FROM 
    orders_table
JOIN 
    dim_store_details ON orders_table.store_code = dim_store_details.store_code
GROUP BY 
    location
ORDER BY 
    number_of_sales;

--------------------------------------------------------
-- Task 5 -- Number of sales of each store type and their percentage of total sales --
SELECT 
    dim_store_details.store_type,
    SUM(product_quantity * dim_products.product_price) as total_sales,
    SUM(product_quantity * dim_products.product_price)/(SUM(SUM(product_quantity * dim_products.product_price)) over ()) * 100 AS percentage_total
FROM 
    orders_table
JOIN 
    dim_store_details ON orders_table.store_code = dim_store_details.store_code
JOIN 
    dim_products ON orders_table.product_code = dim_products.product_code
GROUP BY 
    dim_store_details.store_type
ORDER BY 
    total_sales DESC;

--------------------------------------------------------
-- Task 6 -- Number of sales in each month of each year in descending order --
SELECT 
    dim_date_times.year,
    dim_date_times.month,
    SUM(product_quantity * dim_products.product_price) as total_sales
FROM 
    orders_table
JOIN 
    dim_date_times ON orders_table.date_uuid = dim_date_times.date_uuid
JOIN 
    dim_products ON orders_table.product_code = dim_products.product_code
GROUP BY 
    dim_date_times.year, dim_date_times.month
ORDER BY 
    total_sales DESC;

--------------------------------------------------------
-- Task 7 -- Number of staff in each operating country --
SELECT 
    country_code,
    SUM(staff_numbers) AS total_staff_numbers
FROM 
    dim_store_details
GROUP BY 
    country_code
ORDER BY 
    total_staff_numbers DESC;

--------------------------------------------------------
-- Task 8 -- Total sales of each store type in Germany
SELECT 
    SUM(product_quantity * dim_products.product_price) as total_sales,
    dim_store_details.country_code,
    dim_store_details.store_type
FROM 
    orders_table
JOIN 
    dim_products ON orders_table.product_code = dim_products.product_code
JOIN 
    dim_store_details ON orders_table.store_code = dim_store_details.store_code
WHERE 
    dim_store_details.country_code = 'DE'
GROUP BY 
    dim_store_details.store_type, dim_store_details.country_code
ORDER BY 
    total_sales;

--------------------------------------------------------
-- Task 9 -- Average time between sales for each year --
SELECT 
    year,
    FORMAT(
        '"hours": %s, "minutes": %s, "seconds": %s',
        FLOOR(average_seconds / 3600),
        FLOOR((average_seconds % 3600) / 60),
        average_seconds % 60
    ) AS actual_time_taken,
    average_seconds
FROM (
    SELECT 
        year,
        COUNT(*) AS total_sales,
        (365 * 24 * 60 * 60) / COUNT(*) AS average_seconds 
    FROM 
        dim_date_times
	WHERE YEAR != '1992' AND YEAR != '2022'
    GROUP BY 
        year
) AS YearlySales
ORDER BY 
    average_seconds DESC
LIMIT 5;