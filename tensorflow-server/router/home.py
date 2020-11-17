# '''
# Description: 描述
# Author: 吴文周
# Github: http://gitlab.yzf.net/wuwenzhou
# Date: 2020-11-17 20:43:24
# LastEditors: 吴文周
# LastEditTime: 2020-11-17 21:15:10
# '''
from router.common import *
home = Blueprint('home', __name__)
@home.route('/getIndexCount')
def getIndexCount():
    indexSum = dataBase.querySum()
    res = {
        'code': code,
        'msg': msg,
        'data':indexSum
    }
    return jsonify(res)
# 查询训练趋势数据
@home.route('getTrainCount')
def getTrainCount():
    indexSum = dataBase.queryTrainCount()
    res = {
        'code': code,
        'msg': msg,
        'data':indexSum
    }
    return jsonify(res)
# 获取消息列表
@home.route('/queryMessage')
def queryMessage():
    result = dataBase.queryMessage()
    res = {
        'code': code,
        'msg': msg,
        'data':result
    }
    return jsonify(res)

# 获取消息列表
@home.route('/queryMessageCount')
def queryMessageCount():
    result = dataBase.queryMessageCount()
    res = {
        'code': code,
        'msg': msg,
        'data':result
    }
    return jsonify(res)
# 重置消息状态
@home.route('/updateMessage')
def updateMessage():
    dataBase.updateMessage()
    res = {
        'code': code,
        'msg': msg,
        'data':"ok"
    }
    return jsonify(res)