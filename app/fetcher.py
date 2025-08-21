import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

class Fetcher():

    def __init__(self):
        self.user = os.getenv('MONGO_USER', 'IRGC')
        self.password = os.getenv('MONGO_PASSWORD', 'iraniraniran')
        self.db = os.getenv('MONGO_DB', 'IranMalDB')
        self.client = MongoClient(f'mongodb+srv://{self.user}:{self.password}@{self.db}.gurutam.mongodb.net/')
        
       
    def get_data(self):
        collection = self.client[self.db].list_collection_names()
        data_list = list(self.client[self.db][collection[0]].find())
        return data_list
    
    
