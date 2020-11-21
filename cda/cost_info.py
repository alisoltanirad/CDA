from .college_scorecard import Dataset

class CostInfo():

    def __init__(self):
        self._dataset = Dataset(path='cda/college_scorecard/college_scorecard.csv')

    def show_costs(self):
        print(self._dataset.costs())
