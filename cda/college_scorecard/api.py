# Data source: College Scorecard
import ssl
import pandas as pd
from .data_processing import DataProcessor

class Dataset:

    def __init__(self, path='https://raw.githubusercontent.com/alisoltanirad/'
                            'CDA/main/cda/college_scorecard/'
                            'college_scorecard.csv'):
        ssl._create_default_https_context = ssl._create_unverified_context
        self._dataset = pd.read_csv(path, dtype='unicode')
        self._data_processor = DataProcessor()
        self.college_names = self._dataset['instnm']
        self.ownership = self._data_processor._ownership_types(
            self._dataset['control']
        )

    def students(self):
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
            'Name': self.college_names,
            'Ownership': self.ownership,
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

    def costs(self):
        net_price_public = self._dataset['npt4_pub']
        net_price_private = self._dataset['npt4_priv']
        attendance_cost = self._dataset['costt4_a']
        tuition_in_state = self._dataset['tuitionfee_in']
        tuition_out_state = self._dataset['tuitionfee_out']

        data = {
            'Name': self.college_names,
            'Ownership': self.ownership,
            'Net_Price_Public': net_price_public,
            'Net_Price_Private': net_price_private,
            'Attendance_Cost': attendance_cost,
            'Tuition_In_State': tuition_in_state,
            'Tuition_Out_State': tuition_out_state,
        }
        return pd.DataFrame(data)

    def financial_aids(self):
        title_iv = self._data_processor._list_merge(
            self._dataset['num4_pub'],
            self._dataset['num4_priv'],
            self.ownership
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
            'Name': self.college_names,
            'Ownership': self.ownership,
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


class CollegeData(Dataset):

    def __init__(self, path='https://raw.githubusercontent.com/alisoltanirad/'
                            'CDA/main/cda/college_scorecard/'
                            'college_scorecard.csv'):
        Dataset.__init__(self, path)

        self._set_general_info()
        self._set_fiscal_info()
        self._set_evaluation_metrics()

    def get_info(self):
        data = {
            'Name': self.college_names,
            'Ownership': self.ownership,
            'State': self.state,
            'Student_Size': self.student_size,
            'Is_Online_Only': self.online_only,
            'Is_Men_Only': self.men_only,
            'Is_Women_Only': self.women_only,
            'Is_Religious_Affiliate': self.religious_affiliate,
            'Is_For_Profit': self.for_profit,
            'Tuition_Revenue': self.tuition_revenue,
            'Instructional_Expenditure': self.instructional_expenditure,
            'Faculty_Salary': self.faculty_salary,
            'Faculty_Full_Time_Rate': self.faculty_fulltime_rate,
            'Highest_Degree': self.highest_degrees,
        }
        return pd.DataFrame(data)

    def get_evaluation_metrics(self):
        data = {
            'Name': self.college_names,
            'Admission_Rate': self.admission_rates,
            'Completion_Rate_Overall': self.completion_rate_avg,
            'SAT_Scores_Overall': self.sat_scores,
        }
        return pd.DataFrame(data)

    def _set_general_info(self):
        self.state = self._dataset['stabbr']
        self.student_size = self._dataset['ugds']
        self.online_only = self._dataset['distanceonly']
        self.men_only = self._dataset['menonly']
        self.women_only = self._dataset['womenonly']
        self.religious_affiliate = self._data_processor._is_religious_affiliate(
            self._dataset['relaffil']
        )
        self.for_profit = self._data_processor._is_for_profit(
            self._dataset['control']
        )
        self.highest_degrees = self._data_processor._degree_types(
            self._dataset['highdeg']
        )

    def _set_fiscal_info(self):
        self.tuition_revenue = self._dataset['tuitfte']
        self.instructional_expenditure = self._dataset['inexpfte']
        self.faculty_salary = self._dataset['avgfacsal']
        self.faculty_fulltime_rate = self._dataset['pftfac']

    def _set_evaluation_metrics(self):
        self.admission_rates = self._dataset['adm_rate']
        completion_2yr = self._dataset['overall_yr2_n']
        completion_3yr = self._dataset['overall_yr3_n']
        completion_4yr = self._dataset['overall_yr4_n']
        completion_6yr = self._dataset['overall_yr6_n']
        completion_8yr = self._dataset['overall_yr8_n']
        self.completion_rate_avg = self._data_processor._list_average([
            completion_2yr, completion_3yr, completion_4yr, completion_6yr,
            completion_8yr
        ])
        self.sat_scores = self._dataset['sat_avg']


class MetaData:

    def __init__(self, path='https://raw.githubusercontent.com/alisoltanirad/'
                            'CDA/main/cda/college_scorecard/'
                            'college_scorecard_data_dictionary.csv'):
        ssl._create_default_https_context = ssl._create_unverified_context
        self._dataset = pd.read_csv(path)

    def get_attribute_names(self):
        return self._dataset['developer_friendly_name']
