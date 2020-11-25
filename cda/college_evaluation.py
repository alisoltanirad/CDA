from .college_scorecard import Dataset

class CollegeEvaluation():

    def __init__(self):
        self._data = Dataset().evaluation_metrics()

    def show_evaluation_metrics(self):
        print(self._data)
