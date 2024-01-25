#this folder is basically designed to perform some functionality 

import os
import sys
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')

def read_sql_data():

    logging.info('Reading sql data here...')

    try:
        mydb = pymysql.connect(host=host, user=user, password=password, db=db)
        logging.info('Connection from database has been established', mydb)

        #pd.read_sql_query helps us to read our sql data from sql directly
        df = pd.read_sql_query('Select*from student', mydb)
        print(df.head())

        return df

    except Exception as e:
        raise CustomException(e,sys)
