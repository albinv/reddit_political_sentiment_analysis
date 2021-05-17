from file_manager import *
from reddit import get_all_comments_from_subreddit, get_all_comments_from_user
from config import NLTK_STOPWORDS, SAFE_KEY
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models.tools import HoverTool
from cryptography.fernet import Fernet
import re


def clean_comment(comment):
    # regex to filter out things lik links and make surer no weird symbols exist in the comment
    return re.sub(r"(https?://|www)\S+|\w*\d\w*|[^A-Za-z\s.,'’?]+", "", comment)


def perform_preprocessing(comments_list):
    # clean comment and remove stopwords from it
    cleaned_comments = []
    for comment in comments_list:
        cleaned_comment = clean_comment(comment)
        all_lowercase = cleaned_comment.lower()
        # list comprehension to remove all stopwords found in the config file from the comment
        removed_stopwords = [word for word in all_lowercase.split() if word not in NLTK_STOPWORDS]
        cleaned_comments.append(' '.join(removed_stopwords))
    return cleaned_comments


def get_comments_and_make_file_from_subreddit(subreddit_name, num_posts, sort_order, through_search):
    # write the comments found using the subreddit search function to a file
    filename = concat_file_properties_to_filename([subreddit_name, num_posts, sort_order])
    file_contents = read_from_file(filename)
    if not file_contents:
        all_comments = get_all_comments_from_subreddit(subreddit_name, int(num_posts), sort_order, through_search)
        write_to_file(all_comments, filename)


def get_comments_and_make_file_from_username(username, num_comments, encrypted_username):
    # write the comments found using the username search function to a file
    filename = concat_file_properties_to_filename([username, num_comments, str(encrypted_username)])
    file_contents = read_from_file(filename)
    if not file_contents:
        if encrypted_username:
            username = quick_decrypt(username)
        all_comments = get_all_comments_from_user(username, int(num_comments))
        write_to_file(all_comments, filename)


def view_comments(subreddit_name, num_posts, sort_order):
    # get the comments in the file, found using the name and the search params inputted
    filename = concat_file_properties_to_filename([subreddit_name, num_posts, sort_order])
    return read_from_file(filename)


def make_key():
    # generate a key for encryption
    return Fernet.generate_key()


def quick_encrypt(msg):
    # encrypt the msg using the key found in the config
    encoded_msg = msg.encode()
    fernet = Fernet(SAFE_KEY)
    return fernet.encrypt(encoded_msg).decode("utf-8")


def quick_decrypt(msg):
    # decrypt the msg using the key found in the config file
    encrypted = msg.encode()
    fernet = Fernet(SAFE_KEY)
    return fernet.decrypt(encrypted).decode("utf-8")


def make_sentiment_visual(comments_with_predictions, type, name):
    # plot the visual of the political sentiment analysis using the bokeh plot
    title = "Political Sentiment Analysis performed "
    if type == "subreddit":
        title += "on the Subreddit: r/" + name
    elif type == "username_encrypted":
        title += "for the username (encrypted): " + name
    elif type == "username":
        title += "for the username: " + name
    x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,  1]
    y = [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0]
    name = [[], [],  [],  [],  [],  [],  [],  [],  [],  [], []]
    comment = [[], [], [], [], [], [], [], [], [], [], []]
    for comment_elem in comments_with_predictions:
        # round the sentiment (0-1) to 1dp
        rounded_prediction = round(comment_elem[1], 1)
        index = int(rounded_prediction*10)
        y[index] += 1
        name[index].append(comment_elem[0])
        comment[index].append(comment_elem[2])

    source = ColumnDataSource({
        'Sentiment': x,
        'Count': y,
        'Name': name,
        'Comment': comment
    })

    output_file('sample_plot.html')

    p = figure(
        title=title,
        x_axis_label='Left Wing    <--- Sentiment Value --->   Right Wing',
        y_axis_label='Count',
        tools="pan,box_select,zoom_in,zoom_out,save,reset"
    )

    p.line(x='Sentiment', y='Count', line_width=2, source=source)

    hover = HoverTool()
    hover.tooltips = """
        <div>
            <h3> <strong> Sentiment Value: @Sentiment </strong> <h3>
            <div> <strong> Count: </strong>@Count</div>
            <div> <strong> Sample Comments: </strong>"<marquee behavior=\"scroll\" direction=\"left\">@Comment</marquee>"</div>
        </div>
    """
    "<marquee behavior=\"scroll\" direction=\"left\">@Comment</marquee>"
    p.add_tools(hover)
    show(p)
