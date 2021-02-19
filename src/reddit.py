import praw

NUM_POSTS_LIMIT = 1  # max = 100


# todo: support for more than 100 posts
def get_submission_from_subreddit(reddit, subreddit_name):
    """ Returns a list of submission objects found on the specified subreddit """
    # sorters -> relevance, hot, top, new, comments
    # max limit current = 100
    return reddit.subreddit(subreddit_name).hot(limit=NUM_POSTS_LIMIT)


def get_all_comments(comments):
    """ Given a comment object (i.e CommentForest), outputs a list of all the comments in there """
    if comments is None:
        return []
    elif isinstance(comments, praw.models.reddit.more.MoreComments):
        return get_all_comments(comments.comments())
    elif isinstance(comments, praw.models.reddit.comment.Comment):
        replies = comments.replies
        author = None
        if comments.author:
            author = comments.author.name
        return [(comments.body, author), get_all_comments(replies)]
    elif isinstance(comments, praw.models.comment_forest.CommentForest):
        combined = []
        for comment in (comments.list()):
            combined = combined + get_all_comments(comment)
        return combined
    elif isinstance(comments, list):
        combined = []
        for comment in comments:
            combined = combined + get_all_comments(comment)
        return combined
    else:
        print(type(comments))
        print(comments)


def flatten_list(elem):
    """ a better flat_list() function than pythons default implementation for this specific use case """
    if not elem:
        return []
    elif isinstance(elem, tuple):
        return [elem]
    elif isinstance(elem, list):
        combined = []
        for element in elem:
            flat = flatten_list(element)
            if flat:
                combined = combined + flat
        return combined
    else:
        print(type(elem))
        print(elem)


def get_all_comments_from_subreddit(reddit, subreddit_name):
    """ Given a reddit instance and a subreddit name, will fecth all comments from there"""
    comments_acc = set()
    for submission in get_submission_from_subreddit(reddit, subreddit_name):
        comments = get_all_comments(submission.comments)
        comments_acc.update(flatten_list(comments))
    return list(comments_acc)


def get_reddit_instance():
    return praw.Reddit(
        client_id="jshyL9CMgH5nEg",
        client_secret="WEHm5M9WLUd7PzjzydlUUKiHSH1vnw",
        user_agent="sentiment_analysis by u/albinv1"
    )
