from fetcher import Fetcher
from processor import Processor


class Manager():

    def __init__(self):
        self.list_result = None

    def run(self):
        weapon_list = self.read_txt_file()
        fetcher = Fetcher()
        data = fetcher.get_data()

        processor = Processor(data, weapon_list)
        data = processor.run()

        self.list_result = self.create_list_result(data)

    def read_txt_file(self):
        with open('data/weapon_list.txt', 'r') as f:
            list_rows = f.read().splitlines()
        return list_rows

    def create_list_result(self, df):
        result = []
        for index, row in df.iterrows():
            tweet = {
                "id": str(row['_id']),
                "original_text": row['Text'],
                "rarest_word": row['rarest_word'],
                "sensetive": row['emotions_rate'],
                "weapons_detected": row['weapons_detected']
            }
            result.append(tweet)
        return result

    def get_data_result(self):
        return self.list_result
