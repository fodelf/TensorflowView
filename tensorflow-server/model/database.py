from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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
    # def __repr__(self):
    #     return "<User(name='%s', fullname='%s', password='%s')>" % (
    #         self.name, self.fullname, self.password)
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

def getDataTypes():
    session = Session()
    dataTypes = session.query(DataType).all()
    return dataTypes