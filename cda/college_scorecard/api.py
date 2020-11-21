# Data source: College Scorecard
import ssl
import pandas as pd
from .data_processing import list_average

class Dataset():

    def __init__(self, path='https://raw.githubusercontent.com/alisoltanirad/'
                            'CDA/main/cda/college_scorecard/'
                            'college_scorecard.csv'):
        ssl._create_default_https_context = ssl._create_unverified_context
        self._dataset = pd.read_csv(path, dtype='unicode')

    def evaluation_metrics(self):
        college_names = self._dataset['instnm']
        admission_rates = self._dataset['adm_rate']
        completion_2yr = self._dataset['overall_yr2_n']
        completion_3yr = self._dataset['overall_yr3_n']
        completion_4yr = self._dataset['overall_yr4_n']
        completion_6yr = self._dataset['overall_yr6_n']
        completion_8yr = self._dataset['overall_yr8_n']
        completion_rate_avg = list_average([
            completion_2yr, completion_3yr, completion_4yr, completion_6yr,
            completion_8yr
        ])
        sat_scores = self._dataset['sat_avg']

        data = {
            'Name': college_names,
            'Admission-Rate': admission_rates,
            'Completion-Rate-Overall': completion_rate_avg,
            'SAT-Scores-Overall': sat_scores,
        }
        return pd.DataFrame(data)

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

    def costs(self):
        net_price_public = self._dataset['npt4_pub']
        net_price_private = self._dataset['npt4_priv']

        data = {
            'Net_Price_Public': net_price_public,
            'Net_Price_Private': net_price_private,
        }
        return pd.DataFrame(data)


class MetaData():

    def __init__(self, path='https://raw.githubusercontent.com/alisoltanirad/'
                            'CDA/main/cda/college_scorecard/'
                            'college_scorecard_data_dictionary.csv'):
        ssl._create_default_https_context = ssl._create_unverified_context
        self._dataset = pd.read_csv(path)

    def get_attribute_names(self):
        return self._dataset['developer_friendly_name']
