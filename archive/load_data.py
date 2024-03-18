# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 16:35:14 2023

@author: liamc
"""

# Program to read in our data

# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import psycopg2
from sqlalchemy import create_engine

# Functions
def column_rename(dataframe):
    '''Rename columns to adhere to SQL standards'''
    for column in dataframe.columns:
        
        new_column = column.lower()
        
        if ' ' in column:
            new_column = new_column.replace(' ', '_')
            
        dataframe.rename(columns={column: new_column}, inplace=True)
            
    return dataframe


# Let's get our data

# Shop Customer Data
customer_data = pd.read_csv('C:/Users/liamc/Desktop/DB project/Shop Customer Data/Customers.csv')

# Urban Ecology Over Time Data
species_observed = pd.read_csv('C:/Users/liamc/Desktop/DB project/Urban Ecology Over Time data sets/species_observed.csv')
scat_percent = pd.read_csv('C:/Users/liamc/Desktop/DB project/Urban Ecology Over Time data sets/scat_data_percent.csv')

# Call column_rename on our dataframes
column_rename(customer_data)
column_rename(scat_percent)
column_rename(species_observed)

Create SQL alchemy engine that connects to the Raspberry Pi database
engine = create_engine('sqlite:///sqlite:///192.168.0.14/database_one.db')
engine = create_engine('postgresql+psycopg2://admin:anson3@192.168.0.14/exampledb.db')

Create SQL tables
customer_data.to_sql('customer_data', con=engine, if_exists='replace', index=False)
scat_percent.to_sql('scat_percent', con=engine, if_exists='replace', index=False)
species_observed.to_sql('species_observed', con=engine, if_exists='replace', index=False)

