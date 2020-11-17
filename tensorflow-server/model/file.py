'''
Description: 描述
Author: 吴文周
Github: http://gitlab.yzf.net/wuwenzhou
Date: 2020-11-17 09:32:11
LastEditors: 吴文周
LastEditTime: 2020-11-17 21:52:41
'''
from model.base import *

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


def getDataList():
    session = Session()
    Files = session.query(File).all()
    result = []
    for f in Files:
        result.append(f.to_json())
    return result

# 删除数据源(关联太多)
def deleteDataById(dataId):
    session = Session()
    fileObj= session.query(File).filter(File.dataId == dataId)
    session.delete(fileObj)
    session.commit()
