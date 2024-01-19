# Mulltinational Retail Data Centralisation (MRDC)

## Project Description
The aim of this project was to centralise retail data extracted from different sources of raw data from the branches in a multi-national retail company. The data was cleaned and a STAR-based schema was created for the database, ensuring each entry was casted to the correct data type, and had relations between the tables. The goal of this is to streamline data analysis and reporting across the company, ensuring up-to-date and accurate metrics for the business.

## Installation Instructions
1. First please ensure you have installed:
    - Python (version 3.0 or later)
    - Database system (PostgreSQL has been used for this project) installed and configured
    
2. Clone this repository:
```
git clone https://github.com/CF-Hyett/multinational-retail-data-centralisation766
```
3. Download required libraries in the provided a text file into your enviroment. You can do this with the following command:
```
pip install -r required_libraries.txt
```
4. Create a ```pg_creds.yaml``` for you database in this format:
```
HOST: {your_host_name}
PASSWORD: {your_password}
USER: {your_username}
DATABASE: {your_database}
PORT: {your_port}
```

## Usage Instructions
1. To extract data: Use methods from the DataExtractor class in ```data_extraction.py ```
2. For data cleaning: Use methods from the DataCleaning class in ```data_cleaning.py```
3. To upload data to the database: Use methods from the DatabaseConnector class in ```database_utils.py```
4. Set up Primary Keys and Foreign Key Constraints using the corresponding files
5. Query as required to collect up-to-date metrics of the data

## Project File Structure
- ```Data_Classes_&_Main``` 
    - ```database_utils.py``` contains the class used to read the ```db_creds.yaml``` file to connect to the RDS database retriveing raw data from the sources
    - ```pg_cred.yaml``` to upload extracted data for the STAR-based schem. Ignore in the repo to maintian security
    - ```data_extraction.py ``` contains a class used to extract data from a variety of sources
    - ```data_cleaning.py``` contains a class that is used to clean the data of null and erroneous entries
    - ```run_classes``` files demonstrate the use of the classes for data extraction and cleaning
- ```Database_Building_Queries```
    - ```sales_data.sessions[]``` [1-7] will cast the data to the required  datatypes and [8-9] will set the primary and foreign key constraints
- ```Business_Analysis_Queries```
    - ```sales_data.milestone_4``` contains the queries to retrieve the desired business anlytics


## License Information
This project has no license