#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import uuid
import json
import datetime
from sqlalchemy import (Boolean, Column, DateTime, Float, Integer, String,
                        create_engine, func)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy.pool import SingletonThreadPool
# from model import *
# from dataType import *
Base = declarative_base()
engine = create_engine('sqlite:///tensorflow.db',
  echo=True
)
Session = sessionmaker(bind=engine)
def gen_id():
   return  str(uuid.uuid1())
def gen_time():
   return  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

from model.dataType import *
from model.train import *
from model.model import *

from model.database import *
from model.file import *
from model.message import *

def _init():#初始化
    Base.metadata.create_all(engine)
    session = Session()
    dataTypeFirst = session.query(DataType).first()
    if dataTypeFirst:
      print('data init')
    else:
      dataType1 = DataType(dataName='文件',
            dataId = str(uuid.uuid1()))
      dataType2 = DataType(dataName='数据库',
            dataId = str(uuid.uuid1()))
      session.add_all([dataType1,dataType2])
      session.commit()
      session.close()


# 获取首页汇总
def querySum():
    session =Session()
    sum = {}
    sum['dataSum'] = session.query(File).count()
    sum['modelSum'] = session.query(Model).count()
    sum['trainSum'] = session.query(Train).count()
    sum['resquestSum'] = session.query(Request).count()
    session.close()
    return sum



# 获取数据源汇总
def getDataSum():
    session =Session()
    fileSum = session.query(File).count()
    dataSum = session.query(DataBase).count()
    sum = {}
    sum["total"] = fileSum+dataSum
    sum["menuList"] = []
    child = {'label': '文件','type':'file','count':fileSum}
    sum["menuList"].append(child)
    child = {'label': '数据库','type':'dateBase','count':dataSum}
    sum["menuList"].append(child)
    session.close()
    return sum