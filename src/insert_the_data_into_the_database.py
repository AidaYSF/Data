# Importing necessary libraries
import pandas as pd
from sqlalchemy import create_engine
import os 
import argparse

# Function to insert data into the PostgreSQL database
def insert_the_data_into_the_database(db_url, data_folder_path):

    """
    Inserts data from CSV files into PostgreSQL tables.

    Parameters:
    - db_url (str): The connection URL for the PostgreSQL database, including username, password, host, port, and database name.
    - data_folder_path (str): The path to the folder containing CSV files with data to be inserted.

    Returns:
    None
    """
    
    # Creating a SQLAlchemy engine for the PostgreSQL database
    engine = create_engine(db_url)

    # Reading data from CSV files into pandas DataFrames
    df_cars = pd.read_csv(filepath_or_buffer=os.path.join(data_folder_path, 'car_data.csv'))
    df_consumers = pd.read_csv(filepath_or_buffer=os.path.join(data_folder_path, 'consumer_data.csv'))

    # Resetting the index to obtain integer identifiers
    df_consumers.reset_index(inplace=True)

    # Renaming columns in the consumers DataFrame
    df_consumers.rename(columns={'index': 'Country', 'Country': 'Model', 'Model':'delet'}, inplace=True)
    df_consumers.drop('delet', axis=1, inplace=True)

    # Designing the data model for the PostgreSQL tables
    with engine.connect() as connection:
        # Creating the 'cars' table
        connection.execute('''
            CREATE TABLE IF NOT EXISTS cars (
                id SERIAL PRIMARY KEY,
                make VARCHAR(255),
                model VARCHAR(255),
                year INTEGER,
                price INTEGER,
                engine_type VARCHAR(255)
            )
        ''')

        # Creating the 'consumers' table
        connection.execute('''
            CREATE TABLE IF NOT EXISTS consumers (
                id SERIAL PRIMARY KEY,
                country VARCHAR(255),
                model VARCHAR(255),
                year INTEGER,
                review_score FLOAT,
                sales_volume INTEGER
            )
        ''')

    # Inserting data into the PostgreSQL tables
    df_cars.to_sql('cars', engine, if_exists='replace', index=False)
    df_consumers.to_sql('consumers', engine, if_exists='replace', index=False)

# Checking if the script is executed as the main program
if __name__ == "__main__":
    # Getting the absolute path of the current file
    root =  os.path.dirname(os.path.abspath(__file__))

    # Adding parser arguments for command-line configuration
    parser = argparse.ArgumentParser(
        prog='insert_the_data_into_the_database',
        description='Inserts data into the PostgreSQL database',
        epilog='Text at the bottom of help'
    )
    
    # Adding command-line arguments for database connection and data location
    parser.add_argument('--db_host', type=str, default='localhost', help='Database host')
    parser.add_argument('--db_port', type=int, default=5432, help='Database port')
    parser.add_argument('--db_user', type=str, default='admin', help='Database username')
    parser.add_argument('--db_password', type=str, default='admin', help='Database password')
    parser.add_argument('--database_name', type=str, default='test_db', help='Name of the database')
    parser.add_argument('--data_folder_path', type=str, default=os.path.join(root, '..', 'raw_data'), help='Path to the folder containing data files')

    # Parsing command-line arguments
    args = parser.parse_args()

    # Constructing the PostgreSQL URL based on command-line arguments
    db_url = f'postgresql://{args.db_user}:{args.db_password}@{args.db_host}:{args.db_port}/{args.database_name}'

    # Calling the function to insert data into the database
    try:
        insert_the_data_into_the_database(db_url, args.data_folder_path)
    except Exception as e:
        print(e)
    else: 
        print('files insertion successfully completed.')