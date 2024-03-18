# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 17:02:19 2023

@author: liamc
"""

import pandas as pd
import sqlite3

def column_rename(dataframe):
    '''Rename columns to adhere to SQL standards'''
    for column in dataframe.columns:
        
        if ' ' in column:
            new_column = column.replace(' ', '_').lower()
            dataframe.rename(columns={column: new_column}, inplace=True)
            
    return dataframe

# Example usage
df = pd.DataFrame({'First Name': ['John', 'Jane'], 'Last Name': ['Doe', 'Smith']})
print("Before renaming:")
print(df)

df = column_rename(df)

print("After renaming:")
print(df)


def create_table_from_dataframe(dataframe, table_name, database_name):
    '''Creates a SQLite3 table from a pandas DataFrame'''
    # Connect to the SQLite database
    conn = sqlite3.connect(database_name)
    
    # Create the table
    dataframe.to_sql(table_name, conn, if_exists='replace', index=False)
    
    # Close the database connection
    conn.close()

# Example usage
df = pd.DataFrame({'Name': ['John', 'Jane'], 'Age': [25, 30]})

# Call the function to create a table named 'people' in a database named 'example.db'
create_table_from_dataframe(df, 'people', 'example.db')
