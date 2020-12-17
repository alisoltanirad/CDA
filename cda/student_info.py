from matplotlib import pyplot as plt

from .college_scorecard import StudentData


class StudentInfo:

    def __init__(self, path=None):
        if path == None:
            self._data = StudentData().get_info()
        else:
            self._data = StudentData(path).get_info()

    def get(self):
        return self._data

    def export(self, path='student_data.csv'):
        self._data.to_csv(path, index=False)

    def plot_race_diversity(self):
        categories, numbers = self._get_race_avg()

        plt.style.use('seaborn-talk')
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.bar(categories, numbers)
        fig.canvas.draw()

        n_yticks = len(plt.yticks()[1])
        yticklabels = [
            ''.join([str(i * 10), '%']) for i in range(n_yticks)
        ]
        yticklabels[0] = ''
        ax.set_yticklabels(yticklabels)

        for i, h in enumerate(numbers):
            ax.text(
                i, h + 0.5, ''.join([str(numbers[i]), '%']),
                fontsize=13, horizontalalignment='center'
            )

        ax.set_title('Students Race Diversity')
        plt.show()

    def plot_part_time_share(self):
        categories, numbers = self._get_part_time_share_info()

        plt.style.use('seaborn-talk')
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.pie(numbers, labels=categories, autopct='%1.1f%%', explode=(0, 0.1))
        ax.axis('equal')
        ax.set_title('Students Race Diversity')
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
        numbers = [float('{:.2f}'.format(number))
                   for number in
                   [white, black, hispanic, asian, aian, nhpi, mixed]
        ]

        return categories, numbers

    def _get_part_time_share_info(self):
        part_time = self._data['Part_Time_Share'].astype(float).mean() * 100
        full_time = 100 - part_time

        categories = ['Full-Time', 'Part-Time']
        numbers = [full_time, part_time]

        return categories, numbers
