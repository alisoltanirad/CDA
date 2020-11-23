from .college_scorecard import Dataset

class CollegeInfo():

    def __init__(self):
        self._dataset = Dataset(path='cda/college_scorecard/college_scorecard.csv')

    def show_colleges_info(self):
        print(self._dataset.colleges())