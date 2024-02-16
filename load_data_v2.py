# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 19:15:00 2023

@author: liamc

Program to:
    1. Insert data into SQLite database.
    
    2. Tranfer the tables into pandas dataframes, and convert properties to 
    meet Holywell's SQL style guide.
    
    3. Upload the updated tables to a PostgreSQL database.
    
    4. Plot some of the data on a graph.
    
"""

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import psycopg2


# Define Functions
def column_rename(dataframe):
    """Rename columns to adhere to SQL standards."""
    for column in dataframe.columns:
    
        new_column = column.lower()
        
        if ' ' in new_column:
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

# Create our SQLite database
db_one = sqlite3.connect('db_one')

# Create cursor object
cursor = db_one.cursor()

# Create customers tables from customer_data df
customer_columns = customer_data.columns.tolist()
cursor.execute('''
               CREATE TABLE  customers (
        customerid INTEGER PRIMARY KEY,
        gender TEXT,
        age INTEGER,
        annual_income TEXT,
        spending_score(1-100) INTEGER,
        profession TEXT,
        work_experience TEXT,
        family_size INTEGER
    )
''')

# Insert data into customers table
for _, row in customer_data.iterrows():
    cursor.execute('''
        INSERT INTO customers (customerid, gender, age, annual_income, spending_score, profession, work_experience, family_size) VALUES (?, ?, ?)
    ''', (row['customerid'], row['gender'], row['age'], row['annual_income'], row['spending_score'] ,row['profession'], row['work_experience'], row['family_size']))

# Create the scat percent table
cursor.execute('''
               CREATE TABLE  scat (
        food_source TEXT PRIMARY KEY,
        percent_mass VARCHAR,
    )
''')

# Commit the changes and close the connection to SQLite database
db_one.commit()
db_one.close()

# Transfer tables to pandas dataframes

# Create a connection to the PostgreSQL database
db_two = psycopg2.connect(
    host='localhost',
    port='5432',
    user='your_username',
    password='your_password',
    database='your_database'
)

# Retrieve customers table as a pandas dataframe
customers_df = pd.read_sql('SELECT * FROM customers', db_two)

# Close the connection to the PostgreSQL database
db_two.close()

# Plot some data
plt.plot(species_observed['date'], species_observed['count'])
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Species Observed Over Time')
plt.show()


