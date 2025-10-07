import os 
import sys 
import json 

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
# Do not print the full URL (may contain credentials)
if not MONGO_DB_URL:
    print("MONGO_DB_URL not set in environment (.env) - set it before running the script")

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys) 

    def cv_to_json(self,filepath):
        try:
            data=pd.read_csv(filepath)
            data.reset_index(drop=True,inplace=True)  
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def insert_data_to_mongodb(self,records,database,collection):
        try:
            # preserve provided names but use local variables for DB/collection objects
            self.database = database
            self.collection = collection
            self.client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca, serverSelectionTimeoutMS=5000)
            db = self.client[self.database]
            coll = db[self.collection]
            coll.insert_many(records)
            return len(records)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=="__main__":
    FILE_PATH = os.path.join("Network_Data", "phisingData.csv")
    DATABASE="STARKK"
    Collection="NetworkData"
    obj=NetworkDataExtract()
    records=obj.cv_to_json(FILE_PATH)
    no_of_records=obj.insert_data_to_mongodb(records,DATABASE,Collection)
    print(no_of_records)