import praw

redditInstance = praw.Reddit(
    client_id="jshyL9CMgH5nEg",
    client_secret="WEHm5M9WLUd7PzjzydlUUKiHSH1vnw",
    user_agent="sentiment_analysis by u/albinv1")


# todo support for more than 100 posts
def get_submission_from_subreddit(reddit, subreddit_name):
    # sorters -> relevance, hot, top, new, comments
    # max limit current = 100
    return reddit.subreddit(subreddit_name).hot(limit=1)

#SIMPLE COMMENT EXTRACTION
# def get_all_comments(reddit):
#     all_comments = []
#     for submission in get_submission_from_subreddit(reddit, "learnpython"):
#         print(submission.title)
#         print(submission.selftext)
#         for comment in submission.comments.list():
#             all_comments.append(comment.body)
#     return all_comments


# def get_all_comments(comments):
#     if comments is None:
#         return []
#     if hasattr(comments, "body"):
#         #print(comments.body)
#         return comments.body
#     else:
#         if isinstance(comments, praw.models.reddit.more.MoreComments):
#             more_comments = comments.comments()
#             comments_acc = []
#             for comment in more_comments:
#                 #print(comment.body)
#                 comments_acc.append(comment.body)
#         else:
#             combined = []
#             # comments.replace_more(None, 0),
#             for comment in (comments.list()):
#                 all_comments = get_all_comments(comment)
#                 if all_comments:
#                     combined.append(all_comments)
#                 if isinstance(comments, praw.models.reddit.comment.Comment):
#                     all_replies = get_all_comments(comment.replies)
#                     if all_replies:
#                         combined.append(all_replies)
#             return combined


def get_all_comments(comments):
    if comments is None:
        return []
    if isinstance(comments, praw.models.reddit.more.MoreComments):
        return get_all_comments(comments.comments)
    if isinstance(comments, praw.models.reddit.comment.Comment):
        #comments.refresh()
        replies = comments.replies
        return [comments.body, get_all_comments(replies)]
    if isinstance(comments, praw.models.comment_forest.CommentForest):
        combined = []
        # comments.replace_more(None, 0),
        for comment in (comments.list()):
            combined.append(get_all_comments(comment))
        return combined
    else:
        print(type(comments))
        print(comments)





for submission in get_submission_from_subreddit(redditInstance, "learnpython"):
    print(submission)
    print(submission.title)

    x = get_all_comments(submission.comments)

    for comment in x:
        print(comment)




    # all = get_all_comments(submission.comments)
    # print(all)


    print("\n")
