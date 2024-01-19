SELECT * FROM orders_table;
--------------------------------------------------------

ALTER TABLE orders_table
ALTER COLUMN card_number TYPE VARCHAR(19),
ALTER COLUMN store_code TYPE VARCHAR(20),
ALTER COLUMN product_code TYPE VARCHAR(20),
ALTER COLUMN product_quantity TYPE SMALLINT;

-------------------------------------------------------

-- Add a new column with the correct data type
ALTER TABLE orders_table ADD COLUMN date_uuid_new UUID;

-- Update the new column with the converted values
UPDATE orders_table SET date_uuid_new = CAST(date_uuid AS UUID);

-- Drop the old column
ALTER TABLE orders_table DROP COLUMN date_uuid;

-- Rename the new column to the original column name
ALTER TABLE orders_table RENAME COLUMN date_uuid_new TO date_uuid;

------------------------------------------------------

-- Add a new column with the correct data type
ALTER TABLE orders_table ADD COLUMN user_uuid_new UUID;

-- Update the new column with the converted values
UPDATE orders_table SET user_uuid_new = CAST(user_uuid AS UUID);

-- Drop the old column
ALTER TABLE orders_table DROP COLUMN user_uuid;

-- Rename the new column to the original column name
ALTER TABLE orders_table RENAME COLUMN user_uuid_new TO user_uuid;

-------------------------------------------------------------------

-- Check data types
SELECT column_name, data_type 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE table_name = 'orders_table';


-------------------------------------------------------------------

-- Create a new table with the desired column order
CREATE TABLE orders_table_new AS
SELECT date_uuid, user_uuid, card_number, store_code, product_code, product_quantity
FROM orders_table;

-- Drop the old table
DROP TABLE orders_table;

-- Rename the new table to the original table name
ALTER TABLE orders_table_new RENAME TO orders_table;