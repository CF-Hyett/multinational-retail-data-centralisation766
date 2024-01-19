#%%
from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

# Instantiate classes and run methods
db_connector = DatabaseConnector('db_creds.yaml')
data_extractor = DataExtractor(db_connector)
data_cleaning = DataCleaning(data_extractor)
pg_connector = DatabaseConnector('pg_creds.yaml')
#%%
# Look for orders table name
db_connector.list_db_tables()

# %%
df = data_extractor.read_rds_table('orders_table')
#%%
df.info()
# %%
df = data_cleaning.clean_orders_data(df)
# %%
df.info()
df.head()
# %%
# Upload the cleaned data to the 'sales_data' database in a table named 'orders_table'
pg_connector.upload_to_db(df, 'orders_table')
# %%
