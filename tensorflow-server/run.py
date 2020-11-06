from flask import Flask
from flask import Flask, flash, request, redirect, url_for, jsonify,Response
import time
import random
import string
from werkzeug.utils import secure_filename
import os
import json
import model.database
import service.utils
UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'txt', 'csv'}
app = Flask(__name__,static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'tensorflow'
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

# 新增数据源
@app.route('/api/v1/data/createData', methods=['POST', 'GET'])
def createData():
    t = {
        'code': code,
        'msg': msg,
        'data':{}
    }
    data = request_parse(request)
    file = model.database.File(dataName=data["dataName"],
            dataType=data["dataType"],
            filePath=data["filePath"])
    session = model.database.Session()
    session.add(file)
    session.commit()
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

# 查询数据源列表
@app.route('/api/v1/data/train', methods=['POST'])
def train():
    data = request_parse(request)
    service.utils.train(data)
    res = {
        'code': code,
        'msg': msg,
        'data':'http://127.0.0.1:9567/1.jpg'
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
    dataTypes = model.database.getDataTypes()
    result = []
    for dataType in dataTypes:
        result.append(dataType.to_json())
    res = {
        'code': code,
        'msg': msg,
        'data':result
    }
    return jsonify(res)

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
            mid =  ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 10))
            print(mid)
            print(filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'],filename)
            file.save(filepath)
            return filepath

if __name__ == '__main__':
    app.run(debug=True,
            # host='0.0.0.0',
            port='9567')

