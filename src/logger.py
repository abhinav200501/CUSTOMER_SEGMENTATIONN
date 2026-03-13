import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


'''
logging → Pythons built-in module for recording logs
os → used for working with folders and file paths
datetime → used to generate timestamps

Create a log file name using the current time
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
This creates a unique log file name based on the current date and time.

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.getcwd() → gets the current working directory
"logs" → folder where logs will be stored
LOG_FILE → the log file name

os.makedirs(logs_path,exist_ok=True)
Creates the logs folder
exist_ok=True → prevents errors if the folder already exists

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)
This stores the complete path where logs will be saved.


'''