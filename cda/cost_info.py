from .college_scorecard import Dataset

class CostInfo():

    def __init__(self):
        self._dataset = Dataset()

    def show_costs(self):
        print(self._dataset.costs())
