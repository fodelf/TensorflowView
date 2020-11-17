# '''
# Description: 描述
# Author: 吴文周
# Github: http://gitlab.yzf.net/wuwenzhou
# Date: 2020-11-17 20:43:24
# LastEditors: 吴文周
# LastEditTime: 2020-11-17 21:15:10
# '''
from router.common import *
# 查询训练趋势数据
@data.route('/getDataSum')
def getDataSum():
    dataSum = dataBase.getDataSum()
    res = {
        'code': code,
        'msg': msg,
        'data':dataSum
    }
    return jsonify(res)

# 新增数据源
@data.route('/createData', methods=['POST', 'GET'])
def createData():
    t = {
        'code': code,
        'msg': msg,
        'data':"ok"
    }
    data = request_parse(request)
    dataBase.saveFile(data)
    # session.add(ed_user)
    return jsonify(t)

# 新增数据源
@data.route('/queryTrainById',methods=['POST', 'GET'])
def queryTrainById():
    data = request_parse(request)
    res = dataBase.queryTrainById(data)
    t = {
        'code': code,
        'msg': msg,
        'data': res
    }
    # session.add(ed_user)
    return jsonify(t)
# 解析文件头
@data.route('/parseHeader', methods=['POST', 'GET'])
def parseHeader():
    data = request_parse(request)
    res = service.utils.parseHeader(data["filePath"])
    t = {
        'code': code,
        'msg': msg,
        'data':res
    }
    # session.add(ed_user)
    return jsonify(t)

# 训练
@data.route('/train', methods=['POST'])
def train():
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
  # 查询数据源列表
@data.route('/dataList')
def dataList():
    t = {
        'code': code,
        'msg': msg,
        'data':{}
    }
    return jsonify(t)

# 查询数据类型列表
@data.route('/getDataType')
def getDataType():
    result = dataBase.getDataTypes()
    res = {
        'code': code,
        'msg': msg,
        'data':result
    }
    return jsonify(res)

# 查询数据源列表
@data.route('/getDataList')
def getDataList():
    result = dataBase.getDataList()
    res = {
        'code': code,
        'msg': msg,
        'data':result
    }
    return jsonify(res)

#删除文件数据源
@data.route('/deleteDataById')
def deleteDataById():
    result = dataBase.deleteDataById()
    res = {
        'code': code,
        'msg': msg,
        'data':result
    }
    return jsonify(res)