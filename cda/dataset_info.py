from .college_scorecard import MetaData

class DatasetInfo():

    def __init__(self):
        _dataset_info = MetaData()

    def print_attributes(self):
        print('Attributes:\n', self._dataset_info.get_attribute_names())
