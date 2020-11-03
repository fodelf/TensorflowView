from flask import Flask
from flask import Flask, flash, request, redirect, url_for, jsonify,Response
import time
from werkzeug.utils import secure_filename
import os
import json
import uuid
# from model.database import *
import model.database
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'csv'}
app = Flask(__name__)
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
    print(data)
    file = File(dataName=data["dataName"],
            fileName=data["fileName"],
            filePath=data["filePath"],
            fileSize =data["fileSize"])
    session = getSession()
    session.add(file)
    session.commit()
    # session.add(ed_user)
    return jsonify(t)

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
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            return filepath

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',
            port='9567')

