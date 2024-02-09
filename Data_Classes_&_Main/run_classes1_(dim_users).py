#%%
from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

# Initialize the classes
db_connector = DatabaseConnector('db_creds.yaml')
data_extractor = DataExtractor(db_connector)
data_cleaning = DataCleaning(data_extractor)
pg_connector = DatabaseConnector('pg_creds.yaml')
#%%

# Extract the data
table_name = db_connector.list_db_tables()[1]
print(table_name)
#%%

df = data_extractor.read_rds_table(table_name)
null_count = df.isnull().sum()
print(null_count)
#%%

df_clean = data_cleaning.clean_user_data(df)
#%%

# Upload the cleaned data to the 'sales_data' database in a table named 'dim_users'
pg_connector.upload_to_db(df_clean, 'dim_users')
#%%