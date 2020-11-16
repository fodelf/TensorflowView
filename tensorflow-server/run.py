from flask import Flask
from flask import Flask, flash, request, redirect, url_for, jsonify,Response
from flask_socketio import SocketIO, emit
import time
import random
import string
from werkzeug.utils import secure_filename
import os
import json
import model.database
import service.utils
import  threading
UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'txt', 'csv'}
app = Flask(__name__,static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'tensorflow'
async_mode = None
socketio = SocketIO(app,
            async_handlers=False,
            ping_timeout=60,
            cors_allowed_origins="*",
            always_connect=True,
            async_mode=async_mode
            )
code = 200
msg = 'success'
model.database._init()
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def request_parse(req_data):
    if req_data.method == 'POST':
        data = req_data.json
    elif req_data.method == 'GET':
        data = req_data.args
    return data

# 查询首页汇总数据
@app.route('/api/v1/home/getIndexCount')
def getIndexCount():
    indexSum = model.database.querySum()
    res = {
        'code': code,
        'msg': msg,
        'data':indexSum
    }
    return jsonify(res)

# 查询训练趋势数据
@app.route('/api/v1/home/getTrainCount')
def getTrainCount():
    indexSum = model.database.queryTrainCount()
    res = {
        'code': code,
        'msg': msg,
        'data':indexSum
    }
    return jsonify(res)

# 获取消息列表
@app.route('/api/v1/home/queryMessage')
def queryMessage():
    result = model.database.queryMessage()
    res = {
        'code': code,
        'msg': msg,
        'data':result
    }
    return jsonify(res)
# 获取消息列表
@app.route('/api/v1/home/queryMessageCount')
def queryMessageCount():
    result = model.database.queryMessageCount()
    res = {
        'code': code,
        'msg': msg,
        'data':result
    }
    return jsonify(res)
# 重置消息状态
@app.route('/api/v1/home/updateMessage')
def updateMessage():
    model.database.updateMessage()
    res = {
        'code': code,
        'msg': msg,
        'data':"ok"
    }
    return jsonify(res)    
# 查询训练趋势数据
@app.route('/api/v1/data/getDataSum')
def getDataSum():
    dataSum = model.database.getDataSum()
    res = {
        'code': code,
        'msg': msg,
        'data':dataSum
    }
    return jsonify(res)    
     
# 新增数据源
@app.route('/api/v1/data/createData', methods=['POST', 'GET'])
def createData():
    t = {
        'code': code,
        'msg': msg,
        'data':"ok"
    }
    data = request_parse(request)
    model.database.saveFile(data)
    # session.add(ed_user)
    return jsonify(t)

# 新增数据源
@app.route('/api/v1/data/queryTrainById',methods=['POST', 'GET'])
def queryTrainById():
    data = request_parse(request)
    res = model.database.queryTrainById(data)
    t = {
        'code': code,
        'msg': msg,
        'data': res
    }
    # session.add(ed_user)
    return jsonify(t)
# 解析文件头
@app.route('/api/v1/data/parseHeader', methods=['POST', 'GET'])
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
@app.route('/api/v1/data/train', methods=['POST'])
def train():
    data = request_parse(request)
    if model.database.queryTrainByName(data["trainName"]) == 1:
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

# 训练
@app.route('/api/v1/model/createTrain', methods=['POST'])
def createTrain():
    data = request_parse(request)
    model.database.createTrain(data)
    t = {
        'code': code,
        'msg': msg,
        'data':"ok"
    }
    return jsonify(t)

def thead(data):
    service.utils.train(data,socketio)

# 保存模型
@app.route('/api/v1/model/saveModel', methods=['POST'])
def save():
    data = request_parse(request)
    if model.database.queryModelByName(data["form"]["trainName"]) == 1:
        t = {
        'code': 500,
        'msg': "模型名称已存在",
        'data':"error"
        }
        return jsonify(t)
    model.database.saveModel(data)
    t = {
        'code': code,
        'msg': msg,
        'data':{}
    }
    return jsonify(t)
# 预测试
@app.route('/api/v1/model/preTrain', methods=['POST'])
def test():
    data = request_parse(request)
    res = service.utils.preTrain(data)
    t = {
        'code': code,
        'msg': msg,
        'data':res
    }
    return jsonify(t)

# 预测试
@app.route('/api/v1/model/trainOnline', methods=['POST'])
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
@app.route('/api/v1/model/getParam', methods=['POST'])
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
@app.route('/api/v1/model/getModel')
def getModel():
    result = model.database.queryModel()
    res = {
        'code': code,
        'msg': msg,
        'data':result
    }
    return jsonify(res)

# 查询模型列表
@app.route('/api/v1/model/queryModelList')
def queryModelList():
    result = model.database.queryModelList()
    res = {
        'code': code,
        'msg': msg,
        'data':result
    }
    return jsonify(res)
# 查询模型列表
@app.route('/api/v1/model/queryTrainList')
def queryTrainList():
    result = model.database.queryTrainList()
    res = {
        'code': code,
        'msg': msg,
        'data':result
    }
    return jsonify(res)
# 查询数据源列表
@app.route('/api/v1/data/dataList')
def dataList():
    t = {
        'code': code,
        'msg': msg,
        'data':{}
    }
    return jsonify(t)

# 查询数据类型列表
@app.route('/api/v1/data/getDataType')
def getDataType():
    result = model.database.getDataTypes()
    res = {
        'code': code,
        'msg': msg,
        'data':result
    }
    return jsonify(res)

@socketio.on('mes', namespace='/mes')
def handleMes(json):
    print('received json: ' + str(json))

@socketio.on('connect', namespace='/mes')
def test_connect():
    emit('connect', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/mes')
def test_disconnect():
    print('Client disconnected')

# 查询数据源列表
@app.route('/api/v1/data/getDataList')
def getDataList():
    result = model.database.getDataList()
    res = {
        'code': code,
        'msg': msg,
        'data':result
    }
    return jsonify(res)

# 上传文件功能
@app.route('/api/v1/data/upload', methods=['POST', 'GET'])
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
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.mkdir(app.config['UPLOAD_FOLDER'])
            filepath = os.path.join(app.config['UPLOAD_FOLDER'],filename)
            file.save(filepath)
            fileSize = os.path.getsize(filepath)
            result = {'fileName':filename,'filePath':filepath,'fileSize':fileSize}
            res = {
                'code': code,
                'msg': msg,
                'data':result
            }
            return jsonify(res)

if __name__ == '__main__':
    socketio.run(app,port=9567,debug=True)
    # app.run(debug=True,
    #         # host='0.0.0.0',
    #         port='9567')

