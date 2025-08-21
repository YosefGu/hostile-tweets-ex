from fetcher import Fetcher


class Manager():

    def __init__(self, user='IRGC', password='iraniraniran', db='IranMalDB'):
        self.user = user
        self.password = password
        self.db = db

    def run(self):
        fetcher = Fetcher()
        data = fetcher.get_data(self.user, self.password, self.db)