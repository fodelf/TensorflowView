
from model.base import *
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

def getDataTypes():
    session = Session()
    dataTypes = session.query(DataType).all()
    result = []
    for dataType in dataTypes:
        result.append(dataType.to_json())
    session.close()
    return result
