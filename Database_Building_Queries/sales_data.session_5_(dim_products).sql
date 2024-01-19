SELECT * FROM dim_products;
-----
-- Check data types
SELECT column_name, data_type 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE table_name = 'dim_products';
--------------------------------------------------------
ALTER TABLE dim_products RENAME COLUMN removed TO still_available;
--------------------------------------------------------
ALTER TABLE dim_products ADD COLUMN product_price_new FLOAT;
UPDATE dim_products SET product_price_new = CAST(product_price AS FLOAT);
ALTER TABLE dim_products DROP COLUMN product_price;
ALTER TABLE dim_products RENAME COLUMN product_price_new TO product_price;
--------------------------------------------------------
ALTER TABLE dim_products
    ALTER COLUMN "EAN" TYPE VARCHAR(255),
    ALTER COLUMN product_code TYPE VARCHAR(255);
--------------------------------------------------------

--------------------------------------------------------
ALTER TABLE dim_products ADD COLUMN date_added_new DATE;
UPDATE dim_products SET date_added_new = CAST(date_added AS DATE);
ALTER TABLE dim_products DROP COLUMN date_added;
ALTER TABLE dim_products RENAME COLUMN date_added_new TO date_added;

--------------------------------------------------------
ALTER TABLE dim_products ADD COLUMN uuid_new UUID;
UPDATE dim_products SET uuid_new = CAST(uuid AS UUID);
ALTER TABLE dim_products DROP COLUMN uuid;
ALTER TABLE dim_products RENAME COLUMN uuid_new TO uuid;

--------------------------------------------------------
ALTER TABLE dim_products ADD COLUMN still_available_new BOOL;
UPDATE dim_products SET still_available_new = CAST(still_available AS BOOL);
ALTER TABLE dim_products DROP COLUMN still_available;
ALTER TABLE dim_products RENAME COLUMN still_available_new TO still_available;
--------------------------------------------------------


UPDATE dim_products
SET still_available = CASE
    WHEN still_available = 'Still_avaliable' THEN 'True'
    WHEN still_available = 'Removed' THEN 'False'
    ELSE still_available
END;

