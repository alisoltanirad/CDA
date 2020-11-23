from .college_scorecard import Dataset

class CollegeInfo():

    def __init__(self):
        self._dataset = Dataset()

    def show_colleges_info(self):
        print(self._dataset.colleges())