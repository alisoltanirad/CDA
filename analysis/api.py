import pandas as pd

class Dataset():

    def __init__(self):
        self._dataset = pd.read_csv('../datasets/college_scorecard.csv',
                                    dtype='unicode')


class MetaData():

    def __init__(self):
        self.dataset = pd.read_csv(
            '../datasets/college_scorecard_data_dictionary.csv')


    def get_attributes(self):
        return self._meta_data['developer_friendly_name']
