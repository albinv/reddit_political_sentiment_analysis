from file_manager import *
from reddit import get_reddit_instance, get_all_comments_from_subreddit


def get_comments_and_make_file_from_subreddit(subreddit_name, num_posts, sort_order, through_search):
    reddit_instance = get_reddit_instance()
    filename = concat_file_properties_to_filename(subreddit_name, num_posts, sort_order)
    file_contents = read_from_file(filename)
    if not file_contents:
        all_comments = get_all_comments_from_subreddit(reddit_instance, subreddit_name, int(num_posts), sort_order, through_search)
        write_to_file(all_comments, filename)


def view_comments(subreddit_name, num_posts, sort_order):
    filename = concat_file_properties_to_filename(subreddit_name, num_posts, sort_order)
    return read_from_file(filename)
