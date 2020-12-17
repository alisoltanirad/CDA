import matplotlib.pyplot as plt

from .college_scorecard import CollegeData


class CollegeEvaluation:

    def __init__(self, path=None):
        if path == None:
            self._college_data = CollegeData()
        else:
            self._college_data = CollegeData(path)
        self._college_info = self._college_data.get_info()
        self._evaluation_metrics = self._college_data.get_evaluation_metrics()

    def get(self):
        return self._college_info, self._evaluation_metrics

    def export(self, path='evaluation_data.csv'):
        self._evaluation_metrics.to_csv(path, index=False)

    def plot_tuition_sat(self):
        tuition = self._college_info['Tuition_Revenue'].astype(float)
        sat_scores = self._evaluation_metrics['SAT_Scores_Overall'].astype(float)

        plt.style.use('seaborn-talk')
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.scatter(tuition, sat_scores)
        fig.canvas.draw()

        n_xticks = len(plt.xticks()[1])
        xticklabels = [
            ''.join(['$', str((i - 1) * 10000)]) for i in range(n_xticks)
        ]
        xticklabels[0], xticklabels[1] = '', '0'
        ax.set_xticklabels(xticklabels)

        plt.title('SAT scores correlation with tuition revenue')
        plt.xlabel('Tuition Revenue (Avg.)')
        plt.ylabel('SAT Scores (Overall)')
        plt.show()
