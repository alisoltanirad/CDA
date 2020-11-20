# Data source: College Scorecard
import ssl
import pandas as pd

class Dataset():

    def __init__(self, path='https://raw.githubusercontent.com/alisoltanirad/'
                            'CDA/main/cda/college_scorecard/'
                            'college_scorecard.csv'):
        ssl._create_default_https_context = ssl._create_unverified_context
        self._dataset = pd.read_csv(path, dtype='unicode')

    def evaluation_metrics(self):
        college_names = self._dataset['instnm']
        admission_rates = self._dataset['adm_rate']
        sat_scores = self._dataset['sat_avg']
        completion_rate_4yr = self._dataset['c150_4']
        completion_rate_less_than_4yr = self._dataset['c150_l4']
        #completion_rate_avg = list_average()

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
        data = {'Name': college_names, 'Highest-Degree': highest_degrees}
        return pd.DataFrame(data)


class MetaData():

    def __init__(self, path='https://raw.githubusercontent.com/alisoltanirad/'
                            'CDA/main/cda/college_scorecard/'
                            'college_scorecard_data_dictionary.csv'):
        ssl._create_default_https_context = ssl._create_unverified_context
        self._dataset = pd.read_csv(path)

    def get_attribute_names(self):
        return self._dataset['developer_friendly_name']
