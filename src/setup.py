# This script can be used to setup the required databases
# and tables for the initial setup of the project

import psycopg2 as pg
from psycopg2.errors import ConnectionException
import dotenv
import os
import pandas as pd


class DatabaseWrapper:
    def __init__(self, table_name):
        dotenv.load_dotenv()
        self.table_name = table_name
        USERNAME = os.environ.get("DB_USERNAME")  # Database username
        PASSWORD = os.environ.get("DB_PASSWORD")  # Database password
        DBNAME = os.environ.get("DBNAME")    # Database Name
        HOST = os.environ.get("HOST")
        PORT = os.environ.get("PORT")

        print(USERNAME, PASSWORD, DBNAME, HOST, PORT)

        if PASSWORD is None:
            PASSWORD = ""
        if HOST is None:
            HOST = "localhost"
        if PORT is None:
            PORT = 5432  # Default for PostgreSQL
        if DBNAME is None:
            DBNAME = "ticker_db"

        db_params = {
            'database': DBNAME,
            'user': USERNAME,
            'password': PASSWORD,
            'host': HOST,
            'port': PORT
        }
        # -----------

        try:
            self.connection = pg.connect(**db_params)
            print(f"Connected to DATABASE: {DBNAME}")
        except ConnectionException:
            print("Unable to establish database connection.")
            exit(-1)

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection closed")
        else:
            raise ValueError("Unable to close connection")

    def create_table(self):
        if self.check_if_table_exists():
            print("TABLE Exists")
            return
        cursor = self.connection.cursor()
        cursor.execute(f'''
                       CREATE TABLE {self.table_name} (
                           date TIMESTAMP UNIQUE,
                           close REAL,
                           high REAL,
                           low REAL,
                           open REAL,
                           volume BIGINT,
                           instrument VARCHAR(255)
                           )
                       ''')
        self.connection.commit()
        cursor.close()

    def check_if_table_exists(self):
        cursor = self.connection.cursor()
        # cursor.execute(f'''SELECT EXISTS (SELECT relname FROM pg_class WHERE relname = 'f{self.table_name}')''')
        # cursor.execute(f'''SELECT 1 from {self.table_name}''')
        cursor.execute(f'''SELECT EXISTS(SELECT relname FROM pg_class WHERE relname = '{self.table_name}');''')
        rc = cursor.fetchone()
        return rc[0]

    def load_data_from_xls(self, xls_file_path):
        self.create_table()
        dataframe = pd.read_excel(xls_file_path)
        print(dataframe.columns)
        cursor = self.connection.cursor()
        for _, row in dataframe.iterrows():
            cursor.execute(f'''
                    INSERT INTO {self.table_name}
                    VALUES ('{row['datetime']}', {row['close']}, {row['high']},
                            {row['low']}, {row['open']}, {row['volume']},
                            '{row['instrument']}')
            ''')
            self.connection.commit()

    def get_data_aspd(self):
        dataFrame = pd.read_sql(f"SELECT * FROM {self.table_name}", self.connection)
        return dataFrame

    def empty_table(self):
        curr = self.connection.cursor()
        curr.execute(f'TRUNCATE TABLE {self.table_name}')
        self.connection.commit()
        curr.close()

    def drop_table(self):
        curr = self.connection.cursor()
        curr.execute(f'DROP TABLE {self.table_name}')
        self.connection.commit()
        curr.close()
