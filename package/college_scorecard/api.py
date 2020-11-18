# Data source: College Scorecard
import pandas as pd

class Dataset():

    def __init__(self):
        self._dataset = pd.read_csv('college_scorecard.csv', dtype='unicode')
        self._meta = MetaData()

    def highest_degrees(self):
        degree = {
            '0': "Non-degree-granting",
            '1': "Certificate degree",
            '2': "Associate degree",
            '3': "Bachelor's degree",
            '4': "Graduate degree",
        }
        college_names = self._dataset['instnm']
        highest_degrees = [degree[key] for key in self._dataset['highdeg']]
        data = {'Name': college_names, 'Highest Degree': highest_degrees}
        return pd.DataFrame(data)


class MetaData():

    def __init__(self, path='college_scorecard/college_scorecard_data_dictionary.csv'):
        self._dataset = pd.read_csv(path)

    def get_attribute_names(self):
        return self._dataset['developer_friendly_name']
