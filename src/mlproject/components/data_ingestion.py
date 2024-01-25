## Mysql--> Dataload --> train test split

import os
import sys
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import pandas as pd # to handle and load data


@dataclass 

class DataingestionConfig:
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'raw.csv')

class DataIngestioin:
    def __init__(self):
        self.ingestion = DataingestionConfig()

    def initiate_data_ingestion(self):
        try:
            # i will write a code so that we can load data from sql
            logging.info('Our data from sql has been loaded and read')

            #creating a directory or folder for data
            os.makedirs(os.path.dirname(self.ingestion.train_data_path),exist_ok = True)
        except Exception as e:
            raise CustomException(e,sys)    
    
