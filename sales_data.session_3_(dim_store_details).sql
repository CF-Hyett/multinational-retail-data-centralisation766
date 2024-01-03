SELECT * FROM dim_store_details;
-----
-- Check data types
SELECT column_name, data_type 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE table_name = 'dim_store_details';
--------------------------------------------------------

ALTER TABLE dim_store_details
    ALTER COLUMN longitude TYPE FLOAT,
    ALTER COLUMN locality TYPE VARCHAR(255),
    ALTER COLUMN store_code TYPE VARCHAR(20), -- desired length
    ALTER COLUMN staff_numbers TYPE SMALLINT,
    ALTER COLUMN opening_date TYPE DATE,
    ALTER COLUMN store_type TYPE VARCHAR(255),
    ALTER COLUMN latitude TYPE FLOAT,
    ALTER COLUMN country_code TYPE VARCHAR(2), -- desired length
    ALTER COLUMN continent TYPE VARCHAR(255);

---------------------------------------------------------------

-- Add a new column with the correct data type
ALTER TABLE dim_store_details ADD COLUMN longitude_new FLOAT;

-- Update the new column with the converted values
UPDATE dim_store_details SET longitude_new = CAST(longitude AS FLOAT);

-- Drop the old column
ALTER TABLE dim_store_details DROP COLUMN longitude;

-- Rename the new column to the original column name
ALTER TABLE dim_store_details RENAME COLUMN longitude_new TO longitude;

---------------------------------------------------------------------

-- Add a new column with the correct data type
ALTER TABLE dim_store_details ADD COLUMN staff_numbers_new FLOAT;

-- Update the new column with the converted values
UPDATE dim_store_details SET staff_numbers_new = CAST(staff_numbers AS FLOAT);

-- Drop the old column
ALTER TABLE dim_store_details DROP COLUMN staff_numbers;

-- Rename the new column to the original column name
ALTER TABLE dim_store_details RENAME COLUMN staff_numbers_new TO staff_numbers;

---------------------------------------------------------------------

-- Add a new column with the correct data type
ALTER TABLE dim_store_details ADD COLUMN opening_date_new DATE;

-- Update the new column with the converted values
UPDATE dim_store_details SET opening_date_new = CAST(opening_date AS DATE);

-- Drop the old column
ALTER TABLE dim_store_details DROP COLUMN opening_date;

-- Rename the new column to the original column name
ALTER TABLE dim_store_details RENAME COLUMN opening_date_new TO opening_date;

---------------------------------------------------------------------

-- Add a new column with the correct data type
ALTER TABLE dim_store_details ADD COLUMN latitude_new FLOAT;

-- Update the new column with the converted values
UPDATE dim_store_details SET latitude_new = CAST(latitude AS FLOAT);

-- Drop the old column
ALTER TABLE dim_store_details DROP COLUMN latitude;

-- Rename the new column to the original column name
ALTER TABLE dim_store_details RENAME COLUMN latitude_new TO latitude;

----------------------------------------------------------------------



