from flask import Flask, json
from utils import *

api = Flask(__name__)


def start_server():
    api.run()


@api.route('/check_server_status', methods=['GET'])
def check_running():
    return {"status": 200}

@api.route('/', methods=['GET'])
def check_running():
    return {"status": 200}


@api.route('/get_comments', methods=['GET'])
def get_companies():
    x = []
    for elem in read_from_file("learnpython"):
        x.append({"id": elem[1], "comment": elem[0]})
    json_tmp = {"all_comments": x}
    return json_tmp

