from .college_scorecard import Dataset

class CollegeEvaluation():

    def __init__(self):
        self._dataset = Dataset(path='cda/college_scorecard/college_scorecard.csv')
        self._metrics = self._dataset.evaluation_metrics()

    def show_evaluation_metrics(self):
        print(self._metrics)
