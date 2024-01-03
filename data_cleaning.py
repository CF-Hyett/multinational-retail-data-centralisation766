import pandas as pd
import re
import uuid

class DataCleaning:


    def __init__(self, data_extractor):
        self.data_extractor = data_extractor

    def clean_user_data(self, df):
        
        # Drop rows with NULL values
        df = df.dropna()

        # Convert date columns to datetime format
        for col in df.columns:
            if 'date' in col:
                df[col] = pd.to_datetime(df[col], errors='coerce')

        return df
    
    def clean_card_data(self, df):
        
        # drop rows with NULL values
        df = df.dropna()

        # Clean card_provider column
        values = ['VISA 16 digit', 'JCB 16 digit', 'VISA 13 digit', 'JCB 15 digit', 'VISA 19 digit', 'Diners Club / Carte Blanche', 'American Express', 'Maestro', 'Discover', 'Mastercard']
        df = df[df['card_provider'].isin(values)]

        df['card_number'] = df['card_number'].astype(str)

        df['card_number'] = df['card_number'].str.replace('?', '')

        # Convert date column to datetime format
        df['expiry_date'] = pd.to_datetime(df['expiry_date'], format = '%m/%y', errors = 'coerce')        

        return df 
        
    def clean_store_data(self, df):

        # Reset the index column
        df = df.drop('index', axis=1)

        # Drop mostly NULL erroneous column
        df = df.drop('lat', axis=1)  

        # Clean country_code column
        values = ['US', 'GB', 'DE']
        df = df[df['country_code'].isin(values)]

        # Replace incorrect values in continent column
        df['continent'] = df['continent'].replace('eeEurope', 'Europe')
        df['continent'] = df['continent'].replace('eeAmerica', 'America')
              
        # Define function to convert date formats
        def     convert_dates(date):
            for fmt in ('%Y-%m-%d', '%Y/%m/%d', '%B %Y %d', '%Y %B %d'):
                try:
                    return pd.to_datetime(date, format=fmt)
                except ValueError:
                    continue
            return pd.NaT
        
        # Clean staff_numbers
        df['staff_numbers'] = df['staff_numbers'].str.replace(r'\D', '', regex=True)

        # Apply the function to the 'opening_times' column
        df['opening_date'] = df['opening_date'].apply(convert_dates)

        # Reset the index
        df = df.reset_index(drop=True)

        # Allow null webportal values to change datatypes to FLOAT
        df.iloc[0, 1] = 0
        df.iloc[0, 7] = 0

        return df 

    """convert all product weights to kg"""
    def convert_product_weights(self, df_products):
        self.df_products = df_products
        
        # Function to clean and convert weights
        def convert_weight(weight):
            try:
                # Check if the weight is already in kilograms
                if 'kg' in weight:
                    # Convert to float and remove characters
                    weight = float(re.search(r'\d+\.*\d*', str(weight)).group())
                else:
                    # Handle cases like '8 x 85g', '40 x 100g', etc.
                    if 'x' in weight:
                        parts = weight.split('x')
                        weight = float(parts[0]) * float(''.join(filter(str.isdigit, parts[1]))) / 1000.0
                    else:
                        # Remove excess characters, divide by 1000 and convert to float
                        weight = float(''.join(filter(str.isdigit, str(weight)))) / 1000.0
                
                return weight
            except (ValueError, TypeError, AttributeError):
                # Handle cases where conversion is not possible
                return None
        
        # call convert_weight function 
        df_products['weight'] = df_products['weight'].apply(convert_weight)
        return df_products
    
    def clean_products_data(self, df_products):
        
         # Reset the index column
        df_products.set_index(df_products.columns[0], inplace=True)

        # drop rows with NULL values 
        df_products = df_products.dropna()

         # Remove rows with incorrect data types
        df_products = df_products[pd.to_numeric(df_products['EAN'], errors='coerce').notnull()]

        # Convert date columns to datetime format
        for col in df_products.columns:
            if 'date' in col:
                df_products[col] = pd.to_datetime(df_products[col], errors='coerce')
            return df_products

        return df_products

    
    def clean_orders_data(self, orders_df):
        
        # Drop erroneous columns
        orders_df.drop(['level_0', 'first_name', 'last_name', '1'], axis=1, inplace=True)

        return orders_df
        
    
    def clean_date_times_data(self, df):

        # Clean the timestamp column
        df['timestamp'] = pd.to_datetime(df['timestamp'], format = '%H:%M:%S', errors = 'coerce').dt.time
        
        # Remove rows with incorrect data types
        df['month'] = pd.to_numeric(df['month'], errors = 'coerce')
        df['year'] = pd.to_numeric(df['year'], errors = 'coerce')
        df['day'] = pd.to_numeric(df['day'], errors = 'coerce')
        df = df.astype({'month': 'object', 'year': 'object', 'day': 'object'})
        
        # Clean time_period
        df['time_period'].astype(str)
        df = df[~df['time_period'].str.contains('\d', regex=True)]

        df['date_uuid'].astype(str)
        def is_uuid(column):
            try:
                uuid.UUID(column)
                return True
            except ValueError:
                return False

        mask = df['date_uuid'].apply(is_uuid)
        df = df[mask]

        # drop rows with NULL values 
        df = df.dropna()

        return df
       


    
