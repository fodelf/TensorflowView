from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import uuid
Base = declarative_base()
engine = create_engine('sqlite:///tensorflow.db',echo=True)
Session = sessionmaker(bind=engine)
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
    id = Column(Integer, primary_key=True)
    dataId = Column(String)
    filePath = Column(String)
    dataName = Column(String)
    fileName = Column(String)
    fileSize = Column(String)
    dataType = Column(String)
    def to_json(self):
      dict = self.__dict__
      if "_sa_instance_state" in dict:
          del dict["_sa_instance_state"]
      return dict

class DataType(Base):
    __tablename__ = 'dataType'
    id = Column(Integer, primary_key=True)
    dataName = Column(String , unique=True)
    dataId = Column(String)
    def to_json(self):
      dict = self.__dict__
      if "_sa_instance_state" in dict:
          del dict["_sa_instance_state"]
      return dict

# 模型对象
class Model(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    modelId = Column(String)
    filePath = Column(String)
    modelName = Column(String)
    modelConfig = Column(String)
    def to_json(self):
      dict = self.__dict__
      if "_sa_instance_state" in dict:
          del dict["_sa_instance_state"]
      return dict

def saveModel(data):
    model = Model(dataName=data["modelName"],
          modelConfig=data["modelConfig"],
          filePath=data["filePath"])
    session =Session()
    session.add(model)
    session.commit()

def getDataTypes():
    session = Session()
    dataTypes = session.query(DataType).all()
    return dataTypes

def getDataList():
    session = Session()
    Files = session.query(File).all()
    result = []
    for f in Files:
        result.append(f.to_json())
    return result