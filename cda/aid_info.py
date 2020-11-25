from .college_scorecard import Dataset

class AidInfo():

    def __init__(self):
        self._data = Dataset().financial_aids()

    def show_financial_aids_info(self):
        print(self._data)