#this folder is basically designed to perform some functionality 

import os
import sys
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import mysql.connector
import pickle


def read_sql_data():

    logging.info('Reading sql data here...')

    try:
        mydb = mysql.connector.connect(host='localhost', user='root', password='Honor@2002', db='college')
        logging.info('Connection from database has been established', mydb)

        #pd.read_sql_query helps us to read our sql data from sql directly
        df = pd.read_sql_query('Select*from student', mydb)
        print(df.head())

        return df
    
    except Exception as e:
        raise CustomException(e,sys)
    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)  

    

 