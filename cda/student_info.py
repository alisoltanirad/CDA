from .college_scorecard import Dataset

class StudentInfo():

    def __init__(self):
        self._dataset = Dataset()

    def show_students_info(self):
        print(self._dataset.students())