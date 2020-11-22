# '''
# Description: 描述
# Author: 吴文周
# Github: http://gitlab.yzf.net/wuwenzhou
# Date: 2020-11-17 20:43:24
# LastEditors: 吴文周
# LastEditTime: 2020-11-17 21:15:10
# '''
from router.common import *
model = Blueprint('model', __name__)
# 训练
@model.route('/createTrain', methods=['POST'])
def createTrain():
    data = request_parse(request)
    dataBase.createTrain(data)
    t = {
        'code': code,
        'msg': msg,
        'data':"ok"
    }
    return jsonify(t)

# 保存模型
@model.route('/saveModel', methods=['POST'])
def save():
    data = request_parse(request)
    if dataBase.queryModelByName(data["form"]["trainName"]) == 1:
        t = {
        'code': 500,
        'msg': "模型名称已存在",
        'data':"error"
        }
        return jsonify(t)
    dataBase.saveModel(data)
    t = {
        'code': code,
        'msg': msg,
        'data':{}
    }
    return jsonify(t)
# 预测试
@model.route('/trainOnline', methods=['POST'])
def trainOnline():
    data = request_parse(request)
    res = service.utils.trainOnline(data)
    t = {
        'code': code,
        'msg': msg,
        'data':res
    }
    return jsonify(t)

# 预测试
@model.route('/getParam', methods=['POST'])
def getParam():
    data = request_parse(request)
    res = service.utils.getParam(data)
    t = {
        'code': code,
        'msg': msg,
        'data':res
    }
    return jsonify(t)

# 查询最好和最差模型
@model.route('/getModel')
def getModel():
    result = dataBase.queryModel()
    res = {
        'code': code,
        'msg': msg,
        'data':result
    }
    return jsonify(res)

# 查询模型列表
@model.route('/queryModelList')
def queryModelList():
    data = request_parse(request)
    result = dataBase.queryModelList(data)
    res = {
        'code': code,
        'msg': msg,
        'data':result
    }
    return jsonify(res)
# 查询模型列表
@model.route('/queryTrainList')
def queryTrainList():
    data = request_parse(request)
    result = dataBase.queryTrainList(data)
    res = {
        'code': code,
        'msg': msg,
        'data':result
    }
    return jsonify(res)

# 预测试
@model.route('/deleteModelById', methods=['POST'])
def deleteModelById():
    data = request_parse(request)
    dataBase.deleteModelById(data)
    t = {
        'code': code,
        'msg': msg,
        'data':'ok'
    }
    return jsonify(t)