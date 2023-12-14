#%%
from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

# Instantiate classes and run methods
pg_connector = DatabaseConnector('pg_creds.yaml')
data_extractor = DataExtractor(pg_connector)
data_cleaning = DataCleaning(data_extractor)

s3_address = "s3://data-handling-public/v"
bucket = "data-handling-public"
key = "products.csv"

df = data_extractor.extract_from_s3(bucket, key)
df.head(5)
#%%
df['weight'].value_counts()

# %%
df = data_cleaning.convert_product_weights(df)

#%%
df = data_cleaning.clean_products_data(df)
#%%
df.head(5)
# %%
df.info()
# %%
#df['EAN'].value_counts()
# %%
# Upload the cleaned data to the 'sales_data' database in a table named 'dim_products'
pg_connector.upload_to_db(df, 'dim_products')

# %%
