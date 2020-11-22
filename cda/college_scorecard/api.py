# Data source: College Scorecard
import ssl
import pandas as pd
from .data_processing import *

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
            'Admission_Rate': admission_rates,
            'Completion_Rate_Overall': completion_rate_avg,
            'SAT_Scores_Overall': sat_scores,
        }
        return pd.DataFrame(data)

    def highest_degrees(self):
        college_names = self._dataset['instnm']
        highest_degrees = degree_types(self._dataset['highdeg'])
        data = {'Name': college_names, 'Highest_Degree': highest_degrees}
        return pd.DataFrame(data)

    def costs(self):
        college_names = self._dataset['instnm']
        ownership = ownership_types(self._dataset['control'])
        net_price_public = self._dataset['npt4_pub']
        net_price_private = self._dataset['npt4_priv']
        attendance_cost = self._dataset['costt4_a']
        tuition_in_state = self._dataset['tuitionfee_in']
        tuition_out_state = self._dataset['tuitionfee_out']

        data = {
            'Name': college_names,
            'Ownership': ownership,
            'Net_Price_Public': net_price_public,
            'Net_Price_Private': net_price_private,
            'Attendance_Cost': attendance_cost,
            'Tuition_In_State': tuition_in_state,
            'Tuition_Out_State': tuition_out_state,
        }
        return pd.DataFrame(data)

    def financial_aids(self):
        college_names = self._dataset['instnm']
        ownership = ownership_types(self._dataset['control'])
        federal_loan_rate = self._dataset['pctfloan']
        #x = self._dataset['num4_pub'] or self._dataset['num4_priv']
        a = self._dataset['num4_pub']
        b = self._dataset['num4_priv']
        x = [0 for i in range(len(a))]
        for i in range(len(a)):
            if ownership[i] == 'public':
                x[i] = a[i]
            else:
                x[i] = b[i]

        data = {
            #'Name': college_names,
            'Ownership': ownership,
            #'Federal_Loan_Rate': federal_loan_rate,
            'x': x,
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
