'''
Description: 描述
Author: 吴文周
Github: http://gitlab.yzf.net/wuwenzhou
Date: 2020-11-17 12:31:41
LastEditors: 吴文周
LastEditTime: 2020-11-17 12:32:55
'''
from model.base import *

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