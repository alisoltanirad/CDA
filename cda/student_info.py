from matplotlib import pyplot as plt
from .college_scorecard import StudentData

class StudentInfo():

    def __init__(self):
        self._data = StudentData().get_info()

    def show_data(self):
        print(self._data)

    def plot_race_diversity(self):
        categories, numbers = self._get_race_avg()

        fig, ax = plt.subplots()
        ax.bar(categories, numbers)
        plt.title('Students Race Diversity')
        plt.show()

    def _get_race_avg(self):
        white = self._data['Race_White'].astype(float).mean() * 100
        black = self._data['Race_Black'].astype(float).mean() * 100
        hispanic = self._data['Race_Hispanic'].astype(float).mean() * 100
        asian = self._data['Race_Asian'].astype(float).mean() * 100
        aian = self._data['Race_AIAN'].astype(float).mean() * 100
        nhpi = self._data['Race_NHPI'].astype(float).mean() * 100
        mixed = self._data['Race_Mixed'].astype(float).mean() * 100

        categories = [
            'White', 'Black', 'Hispanic', 'Asian', 'AIAN', 'NHPI', 'Mixed'
        ]
        numbers = [white, black, hispanic, asian, aian, nhpi, mixed]

        return categories, numbers
