import pandas as pd
import matplotlib.pyplot as plt
from .college_scorecard import Dataset

class DegreeInfo():

    def __init__(self):
        self._dataset = Dataset(path='cda/college_scorecard/college_scorecard.csv')

    def plot_highest_degrees(self):
        data = self._dataset.highest_degrees()['Highest-Degree'].value_counts()

        degrees, numbers = [], []
        for degree, number in data.items():
            degrees.append(degree)
            numbers.append(number)

        fig1, ax1 = plt.subplots()
        ax1.pie(numbers, labels=degrees, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        plt.title('Colleges Highest Degree Awarded')
        plt.show()
