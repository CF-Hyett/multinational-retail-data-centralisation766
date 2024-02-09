#%%
from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

# Instantiate classes and run methods
pg_connector = DatabaseConnector('pg_creds.yaml')
data_extractor = DataExtractor(pg_connector)
data_cleaning = DataCleaning(data_extractor)

url = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json'

#%%

df = data_extractor.extract_json_from_s3(url)
#%%

df.head()
df.info()
df['month'].value_counts()
# %%

cleaned_df = data_cleaning.clean_date_times_data(df)
# %%

cleaned_df.head(20)
#cleaned_df[''].value_counts()
# %%

# Upload the cleaned data to the 'sales_data' database in a table named 'dim_date_times'
pg_connector.upload_to_db(df, 'dim_date_times')
#%%

cleaned_df.info()
# %%
