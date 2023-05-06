import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

## initialize Data_ingestion configuration
@dataclass
class Dataingestionconfig:
    raw_data_path:str=os.path.join('artifact','credit_card_data.csv')
    train_data_path:str=os.path.join('artifact','train.csv')
    test_data_path:str=os.path.join('artifact','test.csv')
    
## Create a class for data_ingestion
class DataIngestion:
    def __init__(self):
        self.ingestion_config = Dataingestionconfig()
        
    def data_ingestion_initiate(self):
        logging.info('Data ingestion method starts')
        try:
            df=pd.read_csv(os.path.join('Notebook/UCI_Credit_Card.csv'))
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            df1=pd.read_csv(os.path.join('Notebook/UCI_Credit_Card.csv'))
            logging.info('Train Test Split')
            train_set,test_set = train_test_split(df1,test_size=0.30)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info('Data Ingestion completed')
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
            
        except Exception as e:
            logging.info('Exception at Data Ingestion stage')
            raise CustomException(e,sys)