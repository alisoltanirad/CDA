from matplotlib import pyplot as plt
from .college_scorecard import CollegeData

class CollegeInfo():

    def __init__(self):
        self._data = CollegeData().get_info()

    def show_data(self):
        print(self._data)

    def plot_gender_exclusive_colleges(self):
        men_only = self._data['Is_Men_Only'].value_counts()['true']
        women_only = self._data['Is_Women_Only'].value_counts()['true']
        other = len(self._data.index) - (men_only + women_only)

        categories = ['Men-Only', 'Women-Only', 'Other']
        numbers = [men_only, women_only, other]

        fig, ax = plt.subplots()
        ax.bar(categories, numbers)
        plt.title('Gender Exclusive Colleges')
        plt.show()

    def plot_highest_degrees(self):
        data = self._data['Highest_Degree'].value_counts()

        degrees, numbers = [], []
        for degree, number in data.items():
            degrees.append(degree)
            numbers.append(number)

        fig, ax = plt.subplots()
        ax.pie(numbers, labels=degrees, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        plt.title('Colleges Highest Degree Awarded')
        plt.show()
