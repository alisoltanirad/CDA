from .college_scorecard import FinancialData

class AidInfo():

    def __init__(self):
        self._data = FinancialData().get_aid_info()

    def show_financial_aids_info(self):
        print(self._data)