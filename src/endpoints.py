from flask import Flask, json, request
from flask_cors import CORS, cross_origin
from utils import *

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
    api_request = request.get_json()
    subreddit_name = api_request["name"]
    num_posts = api_request["num_posts"]
    sort_order = api_request["sort_order"]
    all_replies_option = api_request["all_replies_option"],
    get_comments_and_make_file_from_subreddit(subreddit_name, num_posts, sort_order, all_replies_option[0])
    return {"status": 200}


@api.route('/view_comments', methods=['POST'])
def get_comments_by_subreddit():
    api_request = request.get_json()
    subreddit_name = api_request["name"]
    num_posts = api_request["num_posts"]
    sort_order = api_request["sort_order"]
    all_comments = view_comments(subreddit_name, num_posts, sort_order)
    return {"status": 200, "comments_list": all_comments}

#
# @api.route('/get_comments_by_subreddit1', methods=['POST'])
# def get_comments_by_subreddit_name():
#     api_request = request.get_json()
#     subreddit_name = api_request["name"]
#     num_posts = api_request["num_posts"]
#     sort_order = api_request["sort_order"]
#     through_search = False
#     all_comments = get_comments_and_make_file_from_subreddit(subreddit_name, num_posts, sort_order, through_search)
#     return {"status": 200, "comments_list": all_comments}
