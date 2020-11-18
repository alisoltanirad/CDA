from api import MetaData

def print_dataset_info():
    dataset_info = MetaData()
    print('Attributes:\n', dataset_info.get_attribute_names())
