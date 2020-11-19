import matplotlib.pyplot as plt
from .college_scorecard import Dataset

class DegreeInfo():

    def __init__(self):
        self._dataset = Dataset()

    def plot_highest_degrees(self):
        data = self._dataset.highest_degrees()
        degrees = set(data['Highest-Degree'])
        print(data.count())
        plot_data = {}
        for degree in degrees:
            pass
