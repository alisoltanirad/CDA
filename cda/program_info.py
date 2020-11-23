from .college_scorecard import Dataset

class ProgramInfo():

    def __init__(self):
        self._dataset = Dataset()

    def show_programs_info(self):
        print(self._dataset.programs())