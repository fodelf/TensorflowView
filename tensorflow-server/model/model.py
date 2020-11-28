
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
    time = Column(String,nullable=False, default= gen_time)
    learnType = Column(String)
    mae = Column(Float)
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
          learnType=str(form["learnType"]),
          mae = float((trainData["test"]["mae"])),
          filePath=form["filePath"]
          )
    session = Session()
    session.add(model)
    session.commit()
    session.close()

 # 查询同名模型共个数
def queryModelByName(name):
    session =Session()
    sum = session.query(Model).filter(Model.modelName == name).count()
    session.close()
    return sum

# 查询模型状态
def queryModel():
    session =Session()
    if session.query(Model).count()==0:
        session.close()
        return ""
    else:
        sum = {}
        sum['best'] = session.query(Model).order_by(Model.loss.asc()).first().to_json()
        sum['bad'] = session.query(Model).order_by(Model.loss.desc()).first().to_json()
        session.close()
        return sum

# 查询模型状态
def queryModelById(id):
    session =Session()
    modelObj = session.query(Model).filter(Model.modelId == id).first().to_json()
    session.close()
    return modelObj

# 根据模型列表
def queryModelList(data):
    session = Session()
    models = session.query(Model).filter(Model.learnType == data["learnType"]).order_by(Model.id.desc()).limit(data["pageSize"]).offset((int(data["pageNo"])-1)*int(data["pageSize"]))
    total = session.query(Model).count()
    result = []
    for f in models:
        result.append(f.to_json())
    res = {
      "total":total,
      "list":result
    }
    session.close()
    return res

# 删除训练
def deleteModelById(data):
    session = Session()
    model = session.query(Model).filter(Model.modelId == data["modelId"]).first()
    session.delete(model)
    session.commit()
    session.close()

# 查询训练汇总
def queryModelSum():
    session =Session()
    # total = session.query(Model).count()
    regression = session.query(Model).filter(Model.learnType == 'regression').count()
    classification = session.query(Model).filter(Model.learnType == 'classification').count()
    total = regression + classification
    res ={
      "total":total,
      "list":[
        {
          "label":'分类',
          "count":classification,
          "type":'classification'
        },
        {
          "label":'回归',
          "count":regression,
          "type":'regression'
        }
      ]
    }
    session.close()
    return res
