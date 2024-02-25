# Import packages
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from typing import List, Tuple


def connect_to_db(db_name: str) -> object:
    """Returns a connection object to a SQLite database
    
    Args:
    db_name: name of SQLite database
    
    Returns:
    A connection object to a SQLite database
    """
    engine = create_engine(f'sqlite:///{db_name}.db')
    return engine

def load_tables(table_name: str, con: object) -> None:
    """Returns a Pandas DataFrame when passed the name of SQLite table and a connection object
    
    Args:
    table_name: name of table in SQLite database
    con: sqlalchemy connection object
    
    Returns:
    A Pandas DataFrame for each table name in the list
    """
    table = pd.read_sql(f"SELECT * FROM {table_name};", con)
    return table

def write_to_csv(data: pd.DataFrame, table_name: str) -> None:
    """Writes a Pandas DataFrame to a CSV file
    
    Args:
    data: Pandas DataFrame
    table_name: name of table
    
    Returns:
    None
    """
    data.to_csv(f'./data/{table_name}.csv', index=False)
    return None

with engine.connect() as con:
    for table_name in tables:
        table = load_tables(table, con)
        output = 


# Call the load_tables function on each table