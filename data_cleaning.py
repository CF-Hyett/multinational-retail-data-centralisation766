import pandas as pd
import re

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

        # Remove rows with incorrect data types
        #df = df[pd.to_numeric(df['some_column'], errors='coerce').notnull()]
        return df
    
    def clean_card_data(self, df):
        
        # drop erroneous columns
        df = df.iloc[:, :-2]

        # drop rows with NULL values
        df = df.dropna()

        # Remove rows with incorrect data types
        df = df[pd.to_numeric(df['card_number'], errors='coerce').notnull()]

        # Convert date columns to datetime format
        for col in df.columns:
            if 'date' in col:
                df[col] = pd.to_datetime(df[col], errors='coerce')
        
        return df 
        
    def clean_store_data(self, df):

        # Reset the index column
        df.set_index(df.columns[0], inplace=True)

        # Drop mostly NULL erroneous column
        df = df.drop('lat', axis=1)

        # drop rows with NULL values 
        df = df.dropna()

        # Remove rows with incorrect data types
        df = df[pd.to_numeric(df['staff_numbers'], errors='coerce').notnull()]
        
        # Convert date columns to datetime format
        for col in df.columns:
            if 'date' in col:
                df[col] = pd.to_datetime(df[col], errors='coerce')
            return df
        
        # Drop erroneous rows in columns which should contain no numbers
        columns_to_check = ['locality', 'store_type', 'country_code', 'continent']  
        for col in columns_to_check:
            df = df[~df[col].astype(str).str.contains('\d')]
        
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
        df[pd.to_numeric(df.month, errors = 'coerce').notnull()]
        df[pd.to_numeric(df.year, errors = 'coerce').notnull()]
        df[pd.to_numeric(df.day, errors = 'coerce').notnull()]

        df.date_uuid = df.date_uuid.astype('string')

        # Create a new column ‘date’ that combines year, month, and day columns
        df['date'] = pd.to_datetime(df[['year', 'month', 'day']], errors = 'coerce')

        # Drop old date columns
        df.drop(['month', 'year', 'day'], axis=1, inplace=True)
        
        x = ['Evening', 'Morning', 'Midday', 'Late_Hours']
        df = df[df['time_period'].isin(x)]
        df = df.reset_index(drop=True)
        
        df = df.dropna()

        return df
       


    
