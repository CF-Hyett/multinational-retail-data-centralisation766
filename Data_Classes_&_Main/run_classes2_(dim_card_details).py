#%%
from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

# Initialize the classes
pg_connector = DatabaseConnector('pg_creds.yaml')
data_extractor = DataExtractor(pg_connector)
data_cleaning = DataCleaning(data_extractor)

df = data_extractor.retrieve_pdf_data('https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf')
#%%

df['card_number'] = df['card_number'].str.replace('?', '')
df.info()
#%%

df_clean = data_cleaning.clean_card_data(df)
#%%

df_clean.info()
df_clean.head(10)
#%%

# Upload the cleaned data to the 'sales_data' database in a table named 'dim_card_details'
pg_connector.upload_to_db(df_clean, 'dim_card_details')
# %%
