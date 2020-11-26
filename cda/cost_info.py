from .college_scorecard import FinancialData

class CostInfo():

    def __init__(self):
        self._data = FinancialData().get_cost_info()

    def show_costs(self):
        print(self._data)
