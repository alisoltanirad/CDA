from .college_scorecard import StudentData

class StudentInfo():

    def __init__(self):
        self._data = StudentData().get_info()

    def show_data(self):
        print(self._data)