from .college_scorecard import Dataset

class AidInfo():

    def __init__(self):
        self._dataset = Dataset(path='cda/college_scorecard/college_scorecard.csv')

    def show_financial_aids(self):
        print(self._dataset.financial_aids())