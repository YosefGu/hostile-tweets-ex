from pymongo import MongoClient


class Fetcher():

    def __init__(self, user, password, db):
        self.client = MongoClient(f'mongodb+srv://{user}:{password}@{db}.gurutam.mongodb.net/')
        self.db = db
       
    def get_data(self):
        collection = 'tweets'
        return list(self.client[self.db][collection].find())
    
# if __name__ == '__main__':
#     fetcher = Fetcher()
#     fetcher.get_data()