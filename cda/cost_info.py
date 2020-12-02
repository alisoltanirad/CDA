from .college_scorecard import FinancialData

class CostInfo():

    def __init__(self):
        self._data = FinancialData().get_cost_info()

    def show_data(self):
        print(self._data)

    def _get_net_price_avg(self):
        net_price_avg_public = self._data.loc[
            self._data['Ownership'] == 'public'
        ]['Net_Price'].astype(float).mean()
        net_price_avg_private = self._data.loc[
            self._data['Ownership'] == 'private'
        ]['Net_Price'].astype(float).mean()

        categories = ['Public-Schools', 'Private-Schools']
        numbers = [net_price_avg_public, net_price_avg_private]

        return categories, numbers
