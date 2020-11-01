from flask import Flask
from flask import Flask, flash, request, redirect, url_for, jsonify,Response
import time
from werkzeug.utils import secure_filename
import os
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import uuid
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///tensorflow.db',echo=True)
Session = sessionmaker(bind=engine)

class File(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    dataId = Column(String)
    filePath = Column(String)
    dataName = Column(String)
    fileName = Column(String)
    fileSize = Column(String)
    # def __repr__(self):
    #     return "<User(name='%s', fullname='%s', password='%s')>" % (
    #         self.name, self.fullname, self.password)


UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'csv'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'tensorflow'
code = 200
msg = 'success'
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
@app.route('/api/v1/data/creatData', methods=['POST', 'GET'])
def creatData():
    t = {
        'code': code,
        'msg': msg,
        'data':{}
    }
    data = request_parse(request)
    print(data)
    session = Session()
    file = File(dataName=data["dataName"], 
            fileName=data["fileName"], 
            filePath=data["filePath"],
            fileSize =data["fileSize"])
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

@app.route('/upload', methods=['POST', 'GET'])
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
Base.metadata.create_all(engine)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',
            port='9567')

