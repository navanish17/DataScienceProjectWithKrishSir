import os  #importing ooperatin system to manage all the files
import logging  # to manage all the logs
from datetime import datetime  #to get the time data in log files

#this is to collect time vise log
log_file = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

#creating path means file location for log
log_path = os.path.join(os.getcwd(), "logs", log_file)

#making folder for log
os.makedirs(log_path, exist_ok=True)

LOG_PATH_FILE = os.path.join(log_path, log_file)

logging.basicConfig(
    filename = LOG_PATH_FILE,
    format = "[%(asctime)s] %(lineno)d %(name)s- %(levelname)s - %(message)s",
    level = logging.INFO
    )