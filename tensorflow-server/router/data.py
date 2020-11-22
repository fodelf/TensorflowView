# '''
# Description: 描述
# Author: 吴文周
# Github: http://gitlab.yzf.net/wuwenzhou
# Date: 2020-11-17 20:43:24
# LastEditors: 吴文周
# LastEditTime: 2020-11-17 21:15:10
# '''
from router.common import *
from werkzeug.utils import secure_filename
import os
import service.utils
import sys
sys.path.append('..')
import run
# module = __import__('tensorflow-server')
# import tensorflow-server.run as app
ALLOWED_EXTENSIONS = {'txt', 'csv'}
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
    data = request_parse(request)
    result = dataBase.getDataList(data)
    res = {
        'code': code,
        'msg': msg,
        'data':result
    }
    return jsonify(res)

# 查询数据源列表
@data.route('/getDataAll')
def getDataAll():
    result = dataBase.getDataAll()
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

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 上传文件功能
@data.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return 'No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if not os.path.exists('static'):
                os.mkdir('static')
            filepath = os.path.join('static',filename)
            file.save(filepath)
            fileSize = os.path.getsize(filepath)
            result = {'fileName':filename,'filePath':filepath,'fileSize':fileSize}
            res = {
                'code': code,
                'msg': msg,
                'data':result
            }
            return jsonify(res)