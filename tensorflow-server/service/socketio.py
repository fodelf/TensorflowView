#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@Description: 描述
@Author: 吴文周
@Github: http://gitlab.yzf.net/wuwenzhou
@Date: 2020-05-25 15:28:10
LastEditors: 吴文周
LastEditTime: 2020-11-11 21:27:08
'''
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from datetime import datetime
import time
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('task')
def test_message(message):
    print('ssss')
    emit('taskMes', {'data': 'fail'})

if __name__ == '__main__':
    socketio.run(app,port=5000)