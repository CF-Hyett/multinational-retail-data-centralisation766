#%%
import yaml
from sqlalchemy import create_engine, inspect

class DatabaseConnector:

    def __init__(self, filename):
        self.filename = filename
        self.db_creds = self.read_db_creds()
        self.engine = self.init_db_engine()
        self.table_names = self.list_db_tables()
        
    def read_db_creds(self):
         with open(self.filename, 'r') as file:
            db_creds = yaml.safe_load(file)
         return db_creds

    def init_db_engine(self):
        # Create the SQLAlchemy engine
        db_url = f"postgresql://{self.db_creds['RDS_USER']}:{self.db_creds['RDS_PASSWORD']}@{self.db_creds['RDS_HOST']}:{self.db_creds['RDS_PORT']}/{self.db_creds['RDS_DATABASE']}"
        engine = create_engine(db_url)
        return engine
    
    def list_db_tables(self):
        inspector = inspect(self.engine)
        table_names = inspector.get_table_names()
        return table_names

    def upload_to_db(self, df, table_name):
        df.to_sql(table_name, self.engine, if_exists='replace', index=False)

#%%