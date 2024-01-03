SELECT * FROM dim_card_details;
-----
-- Check data types
SELECT column_name, data_type 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE table_name = 'dim_card_details';
--------------------------------------------------------

ALTER TABLE dim_card_details
    ALTER COLUMN card_number TYPE VARCHAR(20),
    ALTER COLUMN expiry_date TYPE VARCHAR(25);
--------------------------------------------------------

ALTER TABLE dim_card_details ADD COLUMN date_payment_confirmed_new DATE;
UPDATE dim_card_details SET date_payment_confirmed_new = CAST(date_payment_confirmed AS DATE);
ALTER TABLE dim_card_details DROP COLUMN date_payment_confirmed;
ALTER TABLE dim_card_details RENAME COLUMN date_payment_confirmed_new TO date_payment_confirmed;