import pandas as pd

class Dataset():

    def __init__(self):
        self._data = pd.read_csv('../datasets/college_scorecard.csv', dtype='unicode')
        self._meta_data = pd.read_csv(
            '../datasets/college_scorecard_data_dictionary.csv')
        print(self._meta_data['developer_friendly_name'])


    def get_attributes(self):
        return self._meta_data['developer_friendly_name']
