import time
import uuid
import json
from sqlalchemy import (Boolean, Column, DateTime, Float, Integer, String,
                        create_engine, func)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# from model import *
# from dataType import *
Base = declarative_base()
engine = create_engine('sqlite:///tensorflow.db',echo=True)
Session = sessionmaker(bind=engine)
def gen_id():
   return  str(uuid.uuid1())


from model.dataType import *
from model.train import *
from model.model import *

from model.dataBase import *
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


# 获取首页汇总
def querySum():
    session =Session()
    sum = {}
    sum['dataSum'] = session.query(File).count()
    sum['modelSum'] = session.query(Model).count()
    sum['trainSum'] = session.query(Train).count()
    sum['resquestSum'] = session.query(Request).count()
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
    return sum