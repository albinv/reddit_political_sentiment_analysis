from reddit import get_reddit_instance, get_all_comments_from_subreddit
from file_manager import write_to_file, read_from_file


def make_file_from_subreddit(subreddit_name):
    reddit_instance = get_reddit_instance()
    all_comments = get_all_comments_from_subreddit(reddit_instance, subreddit_name)
    write_to_file(all_comments, subreddit_name)
    comments = read_from_file(subreddit_name)
    print(comments)


make_file_from_subreddit("learnpython")
