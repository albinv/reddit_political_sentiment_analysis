import pickle


def convert_filename_to_dir(filename):
    return "../data/"+filename


def write_to_file(all_comments, filename="comments"):
    current_filename = convert_filename_to_dir(filename)
    with open(current_filename, 'wb') as file:
        pickle.dump(all_comments, file)


def read_from_file(filename):
    current_filename = convert_filename_to_dir(filename)
    with open(current_filename, 'rb') as file:
        data_list = pickle.load(file)
        return data_list
