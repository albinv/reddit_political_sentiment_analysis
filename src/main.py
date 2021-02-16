from reddit import get_reddit_instance, get_all_comments_from_subreddit
from file_manager import write_to_files


def make_file_from_subreddit(subreddit_name):
    reddit_instance = get_reddit_instance()
    all_comments = get_all_comments_from_subreddit(reddit_instance, subreddit_name)
    write_to_files(all_comments, subreddit_name)


make_file_from_subreddit("learnpython")
