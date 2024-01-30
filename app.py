from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys

from src.mlproject.components.data_ingestion import DataIngestioin
from src.mlproject.components.data_ingestion import DataingestionConfig

from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.data_transformation import DataTransformationConfig

if __name__ == "__main__":
    logging.info("this is to test the logging module")

    try:
         #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestioin()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)

    except Exception as e:
        raise CustomException(e,sys)   