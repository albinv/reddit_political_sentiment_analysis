import pickle
import os.path
from config import DATA_PATH


def convert_filename_to_dir(filename):
    return DATA_PATH+filename


def check_file_exists(file_path):
    return os.path.exists(file_path)


def concat_file_properties_to_filename(properties_list):
    filename = ""
    for prop in properties_list:
        filename = filename + prop + "_"
    return filename[:-1]


def write_to_file(all_comments, filename="comments"):
    current_filename = convert_filename_to_dir(filename)
    with open(current_filename, 'wb') as file:
        pickle.dump(all_comments, file)


def read_from_file(filename="comments"):
    current_filename = convert_filename_to_dir(filename)
    if check_file_exists(current_filename):
        with open(current_filename, 'rb') as file:
            data_list = pickle.load(file)
            return data_list
    else:
        return False
