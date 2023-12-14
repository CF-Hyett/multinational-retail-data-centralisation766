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

#df.head(5)
#df.info()
#df['card_number'].value_counts()
print("percentage of missing values in each column:")
df.isna().mean() * 100

#%%

df_clean = data_cleaning.clean_card_data(df)
df_clean.info()

#%%

#df_clean['card_provider'].value_counts()
df_clean['date_payment_confirmed'].value_counts()

#%%

# Upload the cleaned data to the 'sales_data' database in a table named 'dim_card_details'
pg_connector.upload_to_db(df_clean, 'dim_card_details')
# %%
