from .college_scorecard import MetaData


class DatasetInfo:

    def __init__(self, path=None):
        if path == None:
            self._data = MetaData()
        else:
            self._data = MetaData(path)

    def get_attribute_names(self):
        return self._data.get_attribute_names()
