# Project Title: Mulltinational Retail Data Centralisation (MRDC)
###  (multinational-retail-data-centralisation766)

## Table of Contents, if the README file is long

## A description of the project: what it does, the aim of the project, and what you learned
The aim of this project was to centralise retail data extracted from different sources of raw data from the branches in a multi-national retail company. The data was cleaned and a STAR-based schema was created for the database, ensuring each entry was casted to the correct data type, and had relations between the tables. The goal of this is to streamline data analysis and reporting across the company, ensuring up-to-date and accurate metrics for the business.

## Installation Instructions
1. First please ensure you have installed:
    - Python (version 3.x)
    - Database system (e.g., MySQL, PostgreSQL) installed and configured
    
2. Clone this repository:
```
git clone https://github.com/CF-Hyett/multinational-retail-data-centralisation766
```
3. Download required libraries in the provided a text file. You can do this with the following command:
```
pip install -r required_libraries.txt
```

## Usage instructions
1. To extract data: Use methods from the DataExtractor class in ```data_extraction.py ```
2. For data cleaning: Use methods from the DataCleaning class in ```data_cleaning.py```
3. To upload data to the database: Use methods from the DatabaseConnector class in ```database_utils.py```
4. Set up the Foreign Key Constraints using the Foreign Keys folder files.
5. Query as required to collect up-to-date metrics of the data

## File structure of the project
- database_utils.py contains a class that is used to read the 
- db_creds.yaml to connect to the RDS database to retrive raw data sources 
- pg_cred.yaml to upload extracted data for the STAR-based schema
- data_extraction.py contains a class used to extract data from a variety of sources 
- data_cleaning.py contains a class that is used to clean the data of null, erroneous and inconsistent entries.
- foreign_keys.sql


## License information
This project has no license