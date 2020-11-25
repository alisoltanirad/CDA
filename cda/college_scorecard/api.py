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


    def colleges(self):
        college_names = self._dataset['instnm']
        ownership = ownership_types(self._dataset['control'])
        state = self._dataset['stabbr']
        student_size = self._dataset['ugds']
        online_only = self._dataset['distanceonly']
        men_only = self._dataset['menonly']
        women_only = self._dataset['womenonly']
        religious_affiliate = is_religious_affiliate(self._dataset['relaffil'])
        for_profit = is_for_profit(self._dataset['control'])
        tuition_revenue = self._dataset['tuitfte']
        instructional_expenditure = self._dataset['inexpfte']
        faculty_salary = self._dataset['avgfacsal']
        faculty_fulltime_rate = self._dataset['pftfac']

        data = {
            'Name': college_names,
            'Ownership': ownership,
            'State': state,
            'Student_Size': student_size,
            'Is_Online_Only': online_only,
            'Is_Men_Only': men_only,
            'Is_Women_Only': women_only,
            'Is_Religious_Affiliate': religious_affiliate,
            'Is_For_Profit': for_profit,
            'Tuition_Revenue': tuition_revenue,
            'Instructional_Expenditure': instructional_expenditure,
            'Faculty_Salary': faculty_salary,
            'Faculty_Full_Time_Rate': faculty_fulltime_rate,
        }
        return pd.DataFrame(data)


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


    def students(self):
        college_names = self._dataset['instnm']
        ownership = ownership_types(self._dataset['control'])
        part_time_share = self._dataset['pptug_ef']
        race_white = self._dataset['ugds_white']
        race_black = self._dataset['ugds_white']
        race_hispanic = self._dataset['ugds_hisp']
        race_asian = self._dataset['ugds_asian']
        race_aian = self._dataset['ugds_aian']
        race_nhpi = self._dataset['ugds_nhpi']
        race_mixed = self._dataset['ugds_2mor']
        family_income_dependent = self._dataset['dep_inc_n']
        family_income_independent = self._dataset['ind_inc_n']

        data = {
            'Name': college_names,
            'Ownership': ownership,
            'Part_Time_Share': part_time_share,
            'Race-White': race_white,
            'Race-Black': race_black,
            'Race-Hispanic': race_hispanic,
            'Race-Asian': race_asian,
            'Race-AIAN': race_aian,
            'Race-NHPI': race_nhpi,
            'Race-Mixed': race_mixed,
            'Family_Income_Dependent': family_income_dependent,
            'Family_Income_Independent': family_income_independent,
        }
        return pd.DataFrame(data)


    def highest_degrees(self):
        college_names = self._dataset['instnm']
        highest_degrees = degree_types(self._dataset['highdeg'])
        data = {'Name': college_names, 'Highest_Degree': highest_degrees}
        return pd.DataFrame(data)


    def programs(self):
        college_names = self._dataset['instnm']

        data = {
            'Name': college_names,
        }
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
        title_iv = list_merge(
            self._dataset['num4_pub'],
            self._dataset['num4_priv'],
            ownership
        )
        federal_loan_rate = self._dataset['pctfloan']
        debt_overall = self._dataset['debt_mdn_supp']
        debt_completers = self._dataset['grad_debt_mdn']
        debt_noncompleters = self._dataset['wdraw_debt_mdn']
        debt_dependent = self._dataset['dep_debt_mdn']
        debt_independent = self._dataset['ind_debt_mdn']
        family_income_dependent = self._dataset['dep_inc_n']
        family_income_independent = self._dataset['ind_inc_n']

        data = {
            'Name': college_names,
            'Ownership': ownership,
            'Title_IV': title_iv,
            'Federal_Loan_Rate': federal_loan_rate,
            'Debt_Overall': debt_overall,
            'Debt_Completers': debt_completers,
            'Debt_NonCompleters': debt_noncompleters,
            'Debt_Dependent': debt_dependent,
            'Debt_Independent': debt_independent,
            'Family_Income_Dependent': family_income_dependent,
            'Family_Income_Independent': family_income_independent,
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
