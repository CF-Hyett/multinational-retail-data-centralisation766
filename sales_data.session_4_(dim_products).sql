SELECT * FROM dim_products;
-----
-- Check data types
SELECT column_name, data_type 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE table_name = 'dim_products';
--------------------------------------------------------

UPDATE dim_products
SET product_price = REPLACE(product_price, '£', '');

--------------------------------------------------------

ALTER TABLE dim_products
ADD COLUMN weight_class VARCHAR(255);

--------------------------------------------------------

UPDATE dim_products
SET weight_class = CASE
    WHEN weight < 2 THEN 'Light'
    WHEN weight >= 2 AND weight < 40 THEN 'Mid_Sized'
    WHEN weight >= 40 AND weight < 140 THEN 'Heavy'
    ELSE 'Truck_Required'
END;
