'''
Description: 描述
Author: 吴文周
Github: http://gitlab.yzf.net/wuwenzhou
Date: 2020-11-17 09:29:31
LastEditors: 吴文周
LastEditTime: 2020-11-19 20:01:41
'''
from model.base import *

class Train(Base):
    __tablename__ = 'train'
    id = Column(Integer, autoincrement=True, primary_key=True)
    trainId = Column(String,default=gen_id)
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

# 查询训练列表
def queryTrainList(data):
    session = Session()
    trains = session.query(Train).order_by(Train.id.desc()).limit(data["pageSize"]).offset((int(data["pageNo"])-1)*int(data["pageSize"]))
    total = session.query(Train).count()
    result = []
    for f in trains:
      child = f.to_json()
      child['trainConfig']= json.loads(child['trainConfig'])
      result.append(child)
    res={
      "list":result,
      "total":total
    }
    return res

# 根据id查询训练集
def queryTrainById(data):
    session = Session()
    tarins = session.query(Train).filter(Train.dataId ==data["dataId"]).all()
    result = []
    for f in tarins:
        result.append(f.to_json())
    return result

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

# 根据id查询训练对象
def queryTrainByTrainId(data):
    session = Session()
    train = session.query(Train).filter(Train.trainId ==data["trainId"]).first()
    return train.to_json()

# 删除训练
def deleteTrainById(data):
    session = Session()
    train = session.query(Train).filter(Train.trainId == data["trainId"]).first()
    session.delete(train)
    session.commit()