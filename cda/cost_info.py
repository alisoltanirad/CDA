from .college_scorecard import Dataset

class CostInfo():

    def __init__(self):
        self._data = Dataset().costs()

    def show_costs(self):
        print(self._data)
