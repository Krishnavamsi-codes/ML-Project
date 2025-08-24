import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
## DATA INGESTION REQUIRES CERTAIN INPUTS LIKE 

@dataclass
class DataIngestionConfig:
    train_data_path : str = os.path.join('artifacts','train.csv') # data ingestion will save ur train data in that artifacts folder
    test_data_path : str = os.path.join('artifacts','test.csv')
    raw_data_path : str = os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() # the three paths will get saved inside this

    def initiate_data_ingestion(self):
        logging.info("ENTERED THE DATA INGESTION INITIATION METHDO")
        try:
            df=pd.read_csv('notebook\data\StudentsPerformance.csv')
            logging.info("DATASET HAS BEEN READ")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("TRAIN TEST SPLIT INITIATED")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("The data ingestion process is done")
            return (self.ingestion_config.train_data_path,self.ingestion_config.test_data_path)
        
        
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=='__main__':
    obj=DataIngestion()
    obj.initiate_data_ingestion()




