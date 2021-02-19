from utils import *
from sentiment_analysis import perform_analysis
from endpoints import start_server


# code snippet may be useful later on....
# user = reddit.redditor('UserName')

# make_file_from_subreddit("learnpython")
all_comments = read_from_file("learnpython")
perform_analysis(all_comments)
start_server()
