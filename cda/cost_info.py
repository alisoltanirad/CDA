from matplotlib import pyplot as plt

from .college_scorecard import FinancialData


class CostInfo:

    def __init__(self, path=None):
        if path == None:
            self._data = FinancialData().get_cost_info()
        else:
            self._data = FinancialData(path).get_cost_info()

    def get(self):
        return self._data

    def export(self, path='cost_data.csv'):
        self._data.to_csv(path, index=False)

    def plot_net_price_avg(self):
        categories, numbers = self._get_net_price_avg()

        plt.style.use('seaborn-talk')
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.bar(categories, numbers)
        fig.canvas.draw()

        n_yticks = len(plt.yticks()[1])
        yticklabels = [
            ''.join(['$', str(i * 2500)]) for i in range(n_yticks)
        ]
        yticklabels[0] = ''
        ax.set_yticklabels(yticklabels)

        for i, h in enumerate(numbers):
            ax.text(
                i, h + 150, ''.join(['$', str(numbers[i])]),
                fontsize=13, horizontalalignment='center'
            )

        ax.set_title(
            'Net Price\n (Avg. Attendance Cost Minus Avg. Financial Aid)'
        )
        plt.show()

    def _get_net_price_avg(self):
        net_price_avg_public = float('{:.2f}'.format(
            self._data.loc[
                self._data['Ownership'] == 'public'
            ]['Net_Price'].astype(float).mean()
        ))
        net_price_avg_private = float('{:.2f}'.format(
            self._data.loc[
                self._data['Ownership'] == 'private'
            ]['Net_Price'].astype(float).mean()
        ))

        categories = ['Public-Schools', 'Private-Schools']
        numbers = [net_price_avg_public, net_price_avg_private]

        return categories, numbers
