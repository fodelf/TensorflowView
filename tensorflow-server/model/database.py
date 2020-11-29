#!/usr/bin/python
# -*- coding: UTF-8 -*-
from model.base import *

class DataBase(Base):
    __tablename__ = 'dataBases'
    id = Column(Integer,autoincrement=True, primary_key=True)
    dataId = Column(String,default=gen_id)
    userName = Column(String)
    password = Column(String)
    tableName = Column(String)
    def to_json(self):
      dict = self.__dict__
      if "_sa_instance_state" in dict:
          del dict["_sa_instance_state"]
      return dict


class Request(Base):
    __tablename__ = 'request'
    id = Column(Integer, autoincrement=True, primary_key=True)
    time = Column(String,nullable=False, default= gen_time)
    def to_json(self):
      dict = self.__dict__
      if "_sa_instance_state" in dict:
          del dict["_sa_instance_state"]
      return dict
# 新增模型
def createRequest():
    request = Request()
    session = Session()
    session.add(request)
    session.commit()
    session.close()












