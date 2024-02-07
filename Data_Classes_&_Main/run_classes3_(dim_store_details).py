#%%
import pandas as pd
from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
from credentials.x_api_key import x_api_key

# Instantiate classes and run methods
pg_connector = DatabaseConnector('pg_creds.yaml')
data_extractor = DataExtractor(pg_connector)
data_cleaning = DataCleaning(data_extractor)
#%%

# Define API endpoint URLs
number_of_stores_url = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores"
store_details_url = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/"

# Define API header details
header = x_api_key 

number_of_stores = data_extractor.list_number_of_stores(number_of_stores_url, header)
print(number_of_stores)
#%%

stores_df = data_extractor.retrieve_stores_data(store_details_url, header, 451)
#%%
stores_df.info()

#%%
stores_df['country_code'].value_counts()
#%%

cleaned_stores_df = data_cleaning.clean_store_data(stores_df)
#%%

cleaned_stores_df.head()
#%%

# Upload the cleaned data to the 'sales_data' database in a table named 'dim_store_details'
pg_connector.upload_to_db(cleaned_stores_df, 'dim_store_details')
# %%