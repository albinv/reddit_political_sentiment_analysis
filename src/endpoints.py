from flask import Flask, json, request
from flask_cors import CORS, cross_origin
from utils import *
from sentiment_analysis import get_political_sentiment_prediction

api = Flask(__name__)
cors = CORS(api)
api.config['CORS_HEADERS'] = 'Content-Type'


def start_server():
    api.run()


@api.route('/', methods=['GET'])
def ping():
    return {"status": 200}


@api.route('/get_comments_by_subreddit', methods=['POST'])
def get_comments_by_subreddit_name():
    # Endpoint for getting comments for a given subreddit
    # 1. Extract all parameters from the api request
    # 2. Call the server-side function to retrieve all the requested comments
    # 3. return a status code 200 when all comments have been fetched and saved
    api_request = request.get_json()
    subreddit_name = api_request["name"]
    num_posts = api_request["num_posts"]
    sort_order = api_request["sort_order"]
    all_replies_option = api_request["all_replies_option"],
    get_comments_and_make_file_from_subreddit(subreddit_name, num_posts, sort_order, all_replies_option[0])
    return {"status": 200}


@api.route('/view_comments_subreddit', methods=['POST'])
def view_comments_subreddit():
    # Endpoint for viewing all comments for a given subreddit
    # 1. Extract all parameters from the api request
    # 2. Call the server-side function to get all the saved comments
    # 3. return a json format output of all the fields returned as well as all the comments with encrypted usernames
    api_request = request.get_json()
    subreddit_name = api_request["name"]
    num_posts = api_request["num_posts"]
    sort_order = api_request["sort_order"]
    all_comments = view_comments(subreddit_name, num_posts, sort_order)
    return {"status": 200, "fields": ["comment", "username"], "comments_list": all_comments}


@api.route('/analyse_comments_subreddit', methods=['POST'])
def analyse_comments_subreddit():
    # 1. Endpoint that analyses all the comments for the given subreddit
    # 2. Call the server-side function to get all the saved comments and run them through the model
    # 3. return a json format output of all the fields returned as well as all the comments with encrypted usernames
    #     and the sentiment value attached as well ...
    api_request = request.get_json()
    subreddit_name = api_request["name"]
    num_posts = api_request["num_posts"]
    sort_order = api_request["sort_order"]
    all_comments = view_comments(subreddit_name, num_posts, sort_order)
    comments_with_predictions = False
    if all_comments:
        comments_with_predictions = get_political_sentiment_prediction(all_comments)
        make_sentiment_visual(comments_with_predictions, "subreddit", subreddit_name)
        print("Visual Generated")
    return {"status": 200, "fields": ["encrypted username", "political sentiment", "comment"], "comments_list": comments_with_predictions}


@api.route('/get_comments_by_username', methods=['POST'])
def get_comments_by_username():
    # Endpoint for getting comments for a given username
    # 1. Extract all parameters from the api request
    # 2. Call the server-side function to retrieve all the requested comments
    # 3. return a status code 200 when all comments have been fetched and saved
    api_request = request.get_json()
    username = api_request["name"]
    num_comments = api_request["num_comments"]
    encrypted_username = api_request["encrypted_username"]
    get_comments_and_make_file_from_username(username, num_comments, encrypted_username)
    return {"status": 200}


@api.route('/view_comments_username', methods=['POST'])
def view_comments_username():
    # Endpoint for viewing all comments for a given username
    # 1. Extract all parameters from the api request
    # 2. Call the server-side function to get all the saved comments
    # 3. return a json format output of all the fields returned as well as all the comments with the subreddit names
    api_request = request.get_json()
    username = api_request["name"]
    num_comments = api_request["num_comments"]
    encrypted_username = api_request["encrypted_username"]
    all_comments = view_comments(username, num_comments, str(encrypted_username))
    if not all_comments:
        all_comments = False
    return {"status": 200, "fields": ["comment", "subreddit"], "comments_list": all_comments}


@api.route('/analyse_comments_username', methods=['POST'])
def analyse_comments_username():
    # 1. Endpoint that analyses all the comments for the given username
    # 2. Call the server-side function to get all the saved comments and run them through the model
    # 3. return a json format output of all the fields returned as well as all the comments with the subreddit name
    #     and the sentiment value attached as well ...
    api_request = request.get_json()
    username = api_request["name"]
    num_comments = api_request["num_comments"]
    encrypted_username = api_request["encrypted_username"]
    all_comments = view_comments(username, num_comments, str(encrypted_username))
    comments_with_predictions = False
    if all_comments:
        comments_with_predictions = get_political_sentiment_prediction(all_comments)
        name_for_sentiment_function = "username"
        if encrypted_username:
            name_for_sentiment_function += "_encrypted"
        make_sentiment_visual(comments_with_predictions, name_for_sentiment_function, username)
        print("Visual Generated")
    return {"status": 200, "fields": ["Subreddit", "Political Sentiment", "Comment"], "comments_list": comments_with_predictions}
