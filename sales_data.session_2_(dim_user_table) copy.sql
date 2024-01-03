SELECT * FROM dim_users;
--------------------------------------------------------

ALTER TABLE dim_users
    ALTER COLUMN first_name TYPE VARCHAR(255),
    ALTER COLUMN last_name TYPE VARCHAR(255),
    ALTER COLUMN date_of_birth TYPE DATE,
    ALTER COLUMN country_code TYPE VARCHAR(4),
    ALTER COLUMN user_uuid TYPE UUID,
    ALTER COLUMN join_date TYPE DATE;

--------------------------------------------------------

-- Add a new column with the correct data type
ALTER TABLE dim_users ADD COLUMN user_uuid_new UUID;

-- Remove rows with invalid UUID syntax
DELETE FROM dim_users WHERE NOT user_uuid ~ '^[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$';

-- Update the new column with the converted values
UPDATE dim_users SET user_uuid_new = CAST(user_uuid AS UUID);

-- Drop the old column
ALTER TABLE dim_users DROP COLUMN user_uuid;

-- Rename the new column to the original column name
ALTER TABLE dim_users RENAME COLUMN user_uuid_new TO user_uuid;

-----------------------------------------------------------------


-- Create a new table with the desired column order
CREATE TABLE dim_users_new AS
SELECT   first_name, last_name, date_of_birth, country_code, user_uuid, join_date
FROM dim_users;

-- Drop the old table
DROP TABLE dim_users;

-- Rename the new table to the original table name
ALTER TABLE dim_users_new RENAME TO dim_users;

-------------------------------------------------------------------

-- Check data types
SELECT column_name, data_type 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE table_name = 'dim_users';