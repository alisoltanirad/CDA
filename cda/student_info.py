from .college_scorecard import Dataset

class StudentInfo():

    def __init__(self):
        self._data = Dataset().students()

    def show_students_info(self):
        print(self._data)