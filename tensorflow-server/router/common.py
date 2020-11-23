'''
Description: 描述
Author: 吴文周
Github: http://gitlab.yzf.net/wuwenzhou
Date: 2020-11-17 21:32:34
LastEditors: 吴文周
LastEditTime: 2020-11-23 20:44:10
'''
from flask.blueprints import Blueprint
from flask import Flask, flash, request, redirect, url_for, jsonify,Response
import model.base as dataBase
import service.utils
import service.regression
import json
data = Blueprint('data', __name__)
def request_parse(req_data):
    if req_data.method == 'POST':
        data = req_data.json
    elif req_data.method == 'GET':
        data = req_data.args
    return data
code = 200
msg = 'success'