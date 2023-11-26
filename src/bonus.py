# Importation des bibliothèques nécessaires
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import os
import argparse 


def bonnus(db_url):
    """
    Retrieves data from a specified database and creates a bar chart to visualize the number of Electric and Thermal cars sold per year.

    Parameters:
    - db_url (str): The URL or connection string for the database.

    Returns:
    None

    Dependencies:
    - pandas (pd): Data manipulation library.
    - matplotlib.pyplot (plt): Plotting library.
    - sqlalchemy.create_engine: Function to create a database engine for connection.

    """

    # Creating an engine for the database connection
    engine = create_engine(db_url)

    # Defining the SQL query to retrieve the necessary data
    sql_query = """
        SELECT
            "Year",
            "Engine Type",
            COUNT(*) AS car_count
        FROM
            cars
        WHERE
            "Engine Type" IN ('Electric', 'Thermal')
        GROUP BY
            "Year", "Engine Type"
        ORDER BY
            "Year", "Engine Type";
    """

    # Executing the SQL query and reading the results into a Pandas DataFrame
    df = pd.read_sql_query(sql_query, engine)

    # Pivoting the DataFrame for better visualization
    df_pivot = df.pivot(index='Year', columns='Engine Type', values='car_count')

    # Plotting the bar chart
    df_pivot.plot(kind='bar', stacked=False, figsize=(10, 5), color=['skyblue', 'salmon'])

    # Adding titles and labels
    plt.title('Number of Electric vs. Thermal Cars Sold Per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Cars Sold')

    # Displaying the chart
    plt.show()


if '__main__' == __name__:

    # Getting the absolute path of the current file
    root =  os.path.dirname(os.path.abspath(__file__))

    # Adding parser arguments for command-line configuration
    parser = argparse.ArgumentParser(
        prog='Bonnus',
        description=' Retrieves data from a specified database and creates a bar chart to visualize the number of Electric and Thermal cars sold per year.',
        epilog='Text at the bottom of help'
    )

    # Adding command-line arguments for database connection and data location
    parser.add_argument('--db_host', type=str, default='localhost', help='Database host')
    parser.add_argument('--db_port', type=int, default=5432, help='Database port')
    parser.add_argument('--db_user', type=str, default='admin', help='Database username')
    parser.add_argument('--db_password', type=str, default='admin', help='Database password')
    parser.add_argument('--database_name', type=str, default='test_db', help='Name of the database')

    # Parsing command-line arguments
    args = parser.parse_args()

    # Constructing the PostgreSQL URL based on command-line arguments
    db_url = f'postgresql://{args.db_user}:{args.db_password}@{args.db_host}:{args.db_port}/{args.database_name}'

    # Calling the function to insert data into the database
    try:
        bonnus(db_url)
    except Exception as e:
        print(e)
    else: 
        print('Data retrieval and visualization successfully completed.')
