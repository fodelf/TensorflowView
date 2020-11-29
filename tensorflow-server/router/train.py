#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Description: 描述
Author: 吴文周
Github: http://gitlab.yzf.net/wuwenzhou
Date: 2020-11-18 19:22:43
LastEditors: 吴文周
LastEditTime: 2020-11-23 20:05:56
'''
from router.common import *
import  threading
import sys
sys.path.append('..')
import run
train = Blueprint('train', __name__)
@train.route('/queryTrainByTrainId')
def queryTrainByTrainId():
    data = request_parse(request)
    t = dataBase.queryTrainByTrainId(data)
    res = {
        'code': code,
        'msg': msg,
        'data':t
    }
    return jsonify(res)

@train.route('/deleteTrain', methods=['POST'])
def deleteTrainById():
    data = request_parse(request)
    dataBase.deleteTrainById(data)
    res = {
        'code': code,
        'msg': msg,
        'data':"ok"
    }
    return jsonify(res)

@train.route('/trainAction', methods=['POST'])
def trainAction():
    data = request_parse(request)
    if dataBase.queryTrainByName(data["trainName"]) == 1:
        t = {
        'code': 500,
        'msg': "训练名称已存在",
        'data':"error"
        }
        return jsonify(t)
    thead_one = threading.Thread(target=thead, args=(data,))
    thead_one.start()
    t = {
        'code': code,
        'msg': msg,
        'data':"ok"
    }
    return jsonify(t)

def thead(data):
    if data['learnType'] == 'classification':
        service.utils.train(data,run.socketio)
    else:
        service.regression.train(data,run.socketio)

# 预测试
@train.route('/preTrain', methods=['POST'])
def test():
    data = request_parse(request)
    res =''
    form = data["form"]
    if form['learnType'] == 'classification':
        res = service.utils.preTrain(data)
    else:
        res = service.regression.preTrain(data)
    t = {
        'code': code,
        'msg': msg,
        'data':res
    }
    return jsonify(t)

# 预测试
@train.route('/queryTrainSum')
def queryTrainSum():
    data = request_parse(request)
    res = dataBase.queryTrainSum()
    t = {
        'code': code,
        'msg': msg,
        'data':res
    }
    return jsonify(t)
