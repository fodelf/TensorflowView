#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import string
import time

from flask import Flask, Response, flash, jsonify, redirect, request, url_for,render_template
from flask_socketio import SocketIO, emit

import model.base as dataBase
from router.data import data
from router.home import home
from router.model import model
from router.train import train

UPLOAD_FOLDER = 'static'
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
app.register_blueprint(train, url_prefix='/api/v1/train')

@app.route('/')
def index():
    return redirect('index.html')

@socketio.on('mes', namespace='/mes')
def handleMes(json):
    print('received json: ' + str(json))

@socketio.on('connect', namespace='/mes')
def test_connect():
    emit('connect', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/mes')
def test_disconnect():
    print('Client disconnected')
from werkzeug.exceptions import HTTPException

@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e
    res = {
        'code': 500,
        'msg': '服务端异常',
        'data':""
    }
    return jsonify(res)
if __name__ == '__main__':
    socketio.run(app,port=9567,debug=True)
    # app.run(debug=True,
    #         # host='0.0.0.0',
    #         port='9567')

