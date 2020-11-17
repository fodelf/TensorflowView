
from model.base import *

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

# 根据模型列表
def queryModelList():
    session = Session()
    tarins = session.query(Model).all()
    result = []
    for f in tarins:
        result.append(f.to_json())
    return result