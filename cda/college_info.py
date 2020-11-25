from matplotlib import pyplot as plt
from .college_scorecard import Dataset

class CollegeInfo():

    def __init__(self):
        self._data = Dataset().colleges()

    def show_colleges_info(self):
        print(self._data)

    def plot_highest_degrees(self):
        data = self._data['Highest_Degree'].value_counts()

        degrees, numbers = [], []
        for degree, number in data.items():
            degrees.append(degree)
            numbers.append(number)

        fig1, ax1 = plt.subplots()
        ax1.pie(numbers, labels=degrees, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        plt.title('Colleges Highest Degree Awarded')
        plt.show()