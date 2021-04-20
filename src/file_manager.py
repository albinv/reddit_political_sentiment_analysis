import pickle
import os.path
from config import DATA_PATH


def convert_filename_to_dir(filename):
    # prepend the data path variable from config to the filename
    return DATA_PATH+filename


def check_file_exists(file_path):
    return os.path.exists(file_path)


def concat_file_properties_to_filename(properties_list):
    # append all the search parameters onto the filename
    filename = ""
    for prop in properties_list:
        filename = filename + prop + "_"
    return filename[:-1]


def write_to_file(data, filename="comments"):
    # using pickle library write the data to the specified filename
    current_filename = convert_filename_to_dir(filename)
    with open(current_filename, 'wb') as file:
        pickle.dump(data, file)


def read_from_file(filename="comments"):
    # given a filename, reads the pickle data from it
    current_filename = convert_filename_to_dir(filename)
    if check_file_exists(current_filename):
        with open(current_filename, 'rb') as file:
            data_list = pickle.load(file)
            return data_list
    else:
        return False
