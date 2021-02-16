LINES_PER_FILE = 500


def write_to_files(all_comments, filename="comments"):
    current_filename = filename + "_1"

    if len(all_comments) > LINES_PER_FILE:
        comments = all_comments
        with open(filename, 'w') as f:
            for i in range(LINES_PER_FILE):
                f.write("%s\n" % comments[0])
                comments.pop()
            f.close()
        write_to_files(comments, filename)
    else:
        with open(filename, 'w') as f:
            for comment in all_comments:
                f.write("%s\n" % comment)
