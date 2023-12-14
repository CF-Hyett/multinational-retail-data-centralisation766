#%%
import pandas as pd
import tabula
import requests
import boto3

class DataExtractor:
    def __init__(self, db_connector):
        self.db_connector = db_connector
        
    def read_rds_table(self, table_name):
        df = pd.read_sql_table(table_name, self.db_connector.engine, index_col=['index'])
        return df
    
    def retrieve_pdf_data(self, link):
        # read all pages from the PDF document at the given link
        dfs = tabula.read_pdf(link, stream=True, pages='all')
        df = pd.concat(dfs)
        return df

    def list_number_of_stores(self, number_of_stores_url, header):
        # Make API call to retrieve number of stores
        response = requests.get(number_of_stores_url, headers=header)
        number_of_stores = response.json()
        return number_of_stores
    
    def retrieve_stores_data(self, store_details_url, header, number_of_stores):
        # Make API call to retrieve store data
        stores_data = []
        for i in range(0, number_of_stores):
            response = requests.get(store_details_url + str(i), headers=header)
            if response.headers['content-type'] == 'application/json':
                stores_data.append(response.json())
            else:
                print(f"Warning: Received non-JSON response for store {i}")
        stores_df = pd.DataFrame(stores_data)
        return stores_df
    
    def extract_from_s3(self, bucket, key):
        s3 = boto3.client('s3')
        obj = s3.get_object(Bucket=bucket, Key=key)
        df = pd.read_csv(obj['Body'])
        return df
    
    """Extract json from s3 to pandas df"""
    def extract_json_from_s3(self, url):
        response = requests.get(url)

        with open("date_details.json", "wb") as file:
            file.write(response.content)
            
        df_date = pd.read_json("date_details.json")
        
        return df_date


# %%
