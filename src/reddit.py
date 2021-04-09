import praw
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT


def get_all_comments_from_subreddit(subreddit_name, num_posts=1, sort_order="top", all_replies=False):
    """ Given a subreddit name, will fetch all comments from there """
    reddit = get_reddit_instance()
    comments_acc = set()
    for submission in get_submission_from_subreddit(reddit, subreddit_name, num_posts, sort_order):
        if all_replies:
            comments_acc.update(flatten_list(get_all_comments(submission.comments)))
        else:
            comments_acc.update(flatten_list(get_comments(submission.comments)))
    return list(comments_acc)


def get_all_comments_from_user(username, num_comments=25):
    """ Given a username, will fetch the speciefied number of comments for the user """
    reddit = get_reddit_instance()
    redditor = reddit.redditor(username)
    if num_comments == 0:
        num_comments = None
    all_comments = []
    comments = redditor.comments.new(limit=num_comments)
    for comment in comments:
        if comment.body:
            all_comments.append([comment.body, comment.subreddit.display_name])
    submissions = redditor.submissions.new(limit=num_comments)
    for submission in submissions:
        comment = submission.title
        if submission.selftext:
            comment = comment + " " + submission.selftext
        all_comments.append([comment, submission.subreddit.display_name])
    return all_comments


def get_reddit_instance():
    return praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT
    )


def get_submission_from_subreddit(reddit, subreddit_name, num_posts=1, sort_order="top"):
    """ Returns a list of submission objects found on the specified subreddit """
    submissions = reddit.subreddit(subreddit_name)
    if sort_order == "top":
        return submissions.top(limit=num_posts)
    elif sort_order == "hot":
        return submissions.hot(limit=num_posts)
    else:
        return submissions.new(limit=num_posts)


def get_all_comments(comments):
    """ Given a comment object (i.e CommentForest), outputs a list of all the comments in there """
    from utils import quick_encrypt
    if comments is None:
        return []
    elif isinstance(comments, praw.models.reddit.more.MoreComments):
        return get_all_comments(comments.comments())
    elif isinstance(comments, praw.models.reddit.comment.Comment):
        replies = comments.replies
        author = None
        if comments.author:
            author = quick_encrypt(comments.author.name)
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


def get_comments(comments):
    """ Given a comment object (i.e CommentForest), outputs a list of all the comments in there excluding the
    MoreComment objects and replies """
    from utils import quick_encrypt
    if comments is None:
        return []
    elif isinstance(comments, praw.models.reddit.more.MoreComments):
        return []
    elif isinstance(comments, praw.models.reddit.comment.Comment):
        author = None
        if comments.author:
            author = quick_encrypt(comments.author.name)
        return [(comments.body, author)]
    elif isinstance(comments, praw.models.comment_forest.CommentForest):
        combined = []
        for comment in (comments.list()):
            combined = combined + get_comments(comment)
        return combined
    elif isinstance(comments, list):
        return []
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