import pickle
import os.path


def convert_filename_to_dir(filename):
    return "../data/"+filename


def check_file_exists(file_path):
    return os.path.exists(file_path)


def concat_file_properties_to_filename(name, num_posts, sort_order):
    return name + "_" + num_posts + "_" + sort_order


def write_to_file(all_comments, filename="comments"):
    current_filename = convert_filename_to_dir(filename)
    with open(current_filename, 'wb') as file:
        pickle.dump(all_comments, file)


def read_from_file(filename):
    current_filename = convert_filename_to_dir(filename)
    if check_file_exists(current_filename):
        with open(current_filename, 'rb') as file:
            data_list = pickle.load(file)
            return data_list
    else:
        return False
