from .college_scorecard import CollegeData

class CollegeEvaluation():

    def __init__(self):
        self._data = CollegeData().get_evaluation_metrics()

    def show_evaluation_metrics(self):
        print(self._data)
