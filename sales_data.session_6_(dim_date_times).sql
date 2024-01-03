SELECT * FROM dim_date_times;
-----
-- Check data types
SELECT column_name, data_type 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE table_name = 'dim_date_times';
--------------------------------------------------------

ALTER TABLE dim_date_times
    ALTER COLUMN month TYPE VARCHAR(3),
    ALTER COLUMN year TYPE VARCHAR(5),
    ALTER COLUMN day TYPE VARCHAR(3),
    ALTER COLUMN time_period TYPE VARCHAR(20);
--------------------------------------------------------

DELETE FROM dim_date_times
WHERE month IS NULL;
--------------------------------------------------------

-- Add a new column with the correct data type
ALTER TABLE dim_date_times ADD COLUMN date_uuid_new UUID;

-- Update the new column with the converted values
UPDATE dim_date_times 
SET date_uuid_new = CAST(date_uuid AS UUID)
WHERE date_uuid ~ '^[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-4[A-Fa-f0-9]{3}-[89ABab][A-Fa-f0-9]{3}-[A-Fa-f0-9]{12}$';
-- Drop the old column
ALTER TABLE dim_date_times DROP COLUMN date_uuid;

-- Rename the new column to the original column name
ALTER TABLE dim_date_times RENAME COLUMN date_uuid_new TO date_uuid;
-----------------------------------------------------------

ALTER TABLE dim_date_times  ADD COLUMN timestamp_new TIME;
UPDATE dim_date_times SET timestamp_new = CAST(timestamp AS TIME);
ALTER TABLE dim_date_times DROP COLUMN timestamp;
ALTER TABLE dim_date_times RENAME COLUMN timestamp_new TO timestamp;
