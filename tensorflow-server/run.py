from flask import Flask
from flask import Flask, flash, request, redirect, url_for, jsonify,Response
from flask_socketio import SocketIO, emit
import time
import random
import string
from werkzeug.utils import secure_filename
import os
import model.base as dataBase
from router.home import home
from router.data import data
from router.model import model
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
app.register_blueprint(home, url_prefix='/api/v1/home')
app.register_blueprint(data, url_prefix='/api/v1/data')
app.register_blueprint(model, url_prefix='/api/v1/model')
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@socketio.on('mes', namespace='/mes')
def handleMes(json):
    print('received json: ' + str(json))

@socketio.on('connect', namespace='/mes')
def test_connect():
    emit('connect', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/mes')
def test_disconnect():
    print('Client disconnected')

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

