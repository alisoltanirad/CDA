from .college_scorecard import FinancialData

class FinancialAidInfo():

    def __init__(self):
        self._data = FinancialData().get_aid_info()

    def show_data(self):
        print(self._data)