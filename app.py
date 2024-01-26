from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_ingestion import DataIngestioin
from src.mlproject.components.data_ingestion import DataingestionConfig

if __name__ == "__main__":
    logging.info("this is to test the logging module")

    try:
        Data_Ingestion = DataIngestioin()
        #Dataingestion_Config = DataingestionConfig()
        Data_Ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e,sys)   