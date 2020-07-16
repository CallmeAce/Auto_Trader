__author__ = "xuan"

import json
import os
from config.server_config import ServerConfig, server_current_config
from flask import Flask
from flask import request, jsonify
from flask import Blueprint

from controllers.corp_risk_evaluation import *

from controllers.ele_data_interface import ElementDataService

app = Flask(__name__, static_folder='/test/result_test')

project_name = '/' + server_current_config.project_name

api_obj = ElementDataService()

@app.route("/risk_evaluation", methods=['POST'])
def api_corp_evaluation():
    """
    提现审核
    :return:
    """
    raw_data = request.data.decode("utf-8")

    if isinstance(raw_data, str):
        args = json.loads(raw_data)
    else:
        args = raw_data

    data, code = corp_risk_evaluation(args)
    return jsonify(data), code

@app.route(project_name +"/api/ele_news", methods=['POST'])
def api_news():
    """
    :return:
    """
    raw_data = request.data.decode("utf-8")
    print(raw_data)

    if isinstance(raw_data, str):
        args = json.loads(raw_data)
    else:
        args = raw_data


    data, code = api_obj.get_data('news', args)
    return jsonify(data), code


@app.route(project_name +"/api/ele_risk", methods=['POST'])
def api_risk():
    """
    :return:
    """
    raw_data = request.data.decode("utf-8")

    if isinstance(raw_data, str):
        args = json.loads(raw_data)
    else:
        args = raw_data

    data, code = api_obj.get_data('corp_risk', args)
    return jsonify(data), code


@app.route(project_name +"/api/ele_deep", methods=['POST'])
def api_deep():
    """
    :return:
    """
    raw_data = request.data.decode("utf-8")

    if isinstance(raw_data, str):
        args = json.loads(raw_data)
    else:
        args = raw_data

    data, code = api_obj.get_data('corp_deep', args)
    return jsonify(data), code