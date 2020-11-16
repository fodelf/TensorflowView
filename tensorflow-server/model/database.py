import time
import uuid
import json
from sqlalchemy import (Boolean, Column, DateTime, Float, Integer, String,
                        create_engine, func)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///tensorflow.db',echo=True)
Session = sessionmaker(bind=engine)

def gen_id():
   return  str(uuid.uuid1())

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

class File(Base):
    __tablename__ = 'files'
    id = Column(Integer,autoincrement=True, primary_key=True)
    dataId = Column(String,default=gen_id)
    filePath = Column(String)
    dataName = Column(String)
    fileName = Column(String)
    fileSize = Column(String)
    dataType = Column(String)
    time = Column(DateTime,nullable=False, server_default=func.now())
    def to_json(self):
      dict = self.__dict__
      if "_sa_instance_state" in dict:
          del dict["_sa_instance_state"]
      return dict

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

class DataType(Base):
    __tablename__ = 'dataType'
    id = Column(Integer, autoincrement=True,primary_key=True)
    dataName = Column(String , unique=True)
    dataId = Column(String)
    def to_json(self):
      dict = self.__dict__
      if "_sa_instance_state" in dict:
          del dict["_sa_instance_state"]
      return dict

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, autoincrement=True, primary_key=True)
    messageId = Column(String ,default=gen_id)
    trainConfig = Column(String)
    isRead = Column(Integer, default=0)
    time = Column(DateTime,nullable=False, server_default=func.now())
    def to_json(self):
      dict = self.__dict__
      if "_sa_instance_state" in dict:
          del dict["_sa_instance_state"]
      return dict

class Train(Base):
    __tablename__ = 'train'
    id = Column(Integer, autoincrement=True, primary_key=True)
    trainName = Column(String, unique=True)
    dataName = Column(String)
    trainConfig = Column(String)
    dataId = Column(String)
    time = Column(DateTime,nullable=False, server_default=func.now())
    loss = Column(Float)
    accuracy = Column(Float)
    def to_json(self):
      dict = self.__dict__
      if "_sa_instance_state" in dict:
          del dict["_sa_instance_state"]
      return dict

class Request(Base):
    __tablename__ = 'request'
    id = Column(Integer, autoincrement=True, primary_key=True)
    time = Column(DateTime,nullable=False, server_default=func.now())
    def to_json(self):
      dict = self.__dict__
      if "_sa_instance_state" in dict:
          del dict["_sa_instance_state"]
      return dict     
# 模型对象
class Model(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    modelId = Column(String,default=gen_id)
    dataId = Column(String)
    filePath = Column(String)
    modelName = Column(String)
    dataName = Column(String)
    modelConfig = Column(String)
    formConfig = Column(String)
    loss = Column(Float)
    accuracy = Column(Float)
    time = Column(DateTime,nullable=False, server_default=func.now())
    def to_json(self):
      dict = self.__dict__
      if "_sa_instance_state" in dict:
          del dict["_sa_instance_state"]
      return dict

# 新增文件
def saveFile(data):
    fileObj = File(filePath = data["filePath"],
                dataName = data["dataName"],
                fileName = data["fileName"],
                fileSize = data["fileSize"],
                dataType = data["dataType"])
    session = Session()
    session.add(fileObj)
    session.commit()

# 新增模型
def saveModel(data):
    form = data["form"]
    trainData = data["trainData"]
    model = Model(modelName=form["trainName"],
          dataId=form["dataId"],
          dataName=form["dataName"],
          modelConfig=json.dumps(trainData, indent=2),
          formConfig=json.dumps(form, indent=2),
          loss = float(trainData["test"]["loss"]),
          accuracy = float(trainData["test"]["accuracy"]),
          filePath=form["filePath"])
    session = Session()
    session.add(model)
    session.commit()

 # 查询同名模型共个数
def queryModelByName(name):
    session =Session()
    sum = session.query(Model).filter(Model.modelName == name).count()
    return sum   
# 查询模型状态
def queryModel():
    session =Session()
    if session.query(Model).count()==0:
        return ""
    else:    
        sum = {}
        sum['best'] = session.query(Model).order_by(Model.accuracy.desc()).first().to_json()
        sum['bad'] = session.query(Model).order_by(Model.accuracy.asc()).first().to_json()
        return sum

# 查询模型状态
def queryModelById(id):
    session =Session()
    modelObj = session.query(Model).filter(Model.modelId == id).first().to_json()
    return modelObj
   
# 新建训练
def createTrain(data):
    train = Train(trainConfig=json.dumps(data["trainConfig"], indent=2),
                dataName=data["dataName"],
                dataId=str(data["dataId"]),
                loss = float(data["loss"]),
                trainName=str(data["trainName"]),
                accuracy = float(data["accuracy"])
          )
    session = Session()
    session.add(train)
    session.commit()

def getDataTypes():
    session = Session()
    dataTypes = session.query(DataType).all()
    result = []
    for dataType in dataTypes:
        result.append(dataType.to_json())
    return result

def getDataList():
    session = Session()
    Files = session.query(File).all()
    result = []
    for f in Files:
        result.append(f.to_json())
    return result

def createMessage(data):
    message = Message(trainConfig=json.dumps(data['trainConfig'], indent=2))
    session =Session()
    session.add(message)
    session.commit() 

def queryMessage():
    session =Session()
    messages = session.query(Message).filter((Message.isRead == 0)).all()
    result = []
    for f in messages:
        child = f.to_json()
        child['trainConfig']= json.loads(child['trainConfig'])
        result.append(child)
    return result

def queryMessageById(messageId):
    session =Session()
    message = session.query(Message).filter_by(messageId=messageId).first()
    return message.to_json()
# 查询消息总共个数
def queryMessageCount():
    session =Session()
    sum = session.query(Message).filter(Message.isRead == 0).count()
    return sum

# 更新消息读取状态
def updateMessage():
    session =Session()
    session.query(Message).filter(Message.isRead == 0).update({Message.isRead:1})
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


# 训练趋势统计    
def queryTrainCount():
    session = Session()
    tarins = session.query(func.strftime('%Y/%m/%d',Train.time).label('date'),func.count(Train.id).label('count')).group_by('date').limit(7).all()
    # print(tarins)
    # result = []
    # for f in tarins:
    #     result.append(json.dumps(f))
    return tarins

# 查询训练名称是否重复
def queryTrainByName(name):
    session =Session()
    sum = session.query(Train).filter(Train.trainName == name).count()
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

# 根据id查询训练集
def queryTrainById(data):
    session = Session()
    tarins = session.query(Train).filter(Train.dataId ==data["dataId"]).all()
    result = []
    for f in tarins:
        result.append(f.to_json())
    return result

# 根据模型列表
def queryModelList():
    session = Session()
    tarins = session.query(Model).all()
    result = []
    for f in tarins:
        result.append(f.to_json())
    return result

# 查询训练列表
def queryTrainList():
    session = Session()
    tarins = session.query(Train).all()
    result = []
    for f in tarins:
      child = f.to_json()
      child['trainConfig']= json.loads(child['trainConfig'])
      result.append(child)
    return result