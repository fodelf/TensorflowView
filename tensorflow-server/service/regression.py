import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from tensorflow import keras
import json
import tempfile
from tensorflow.keras.callbacks import LearningRateScheduler
from tensorflow import feature_column
from sklearn.model_selection import train_test_split
from sklearn.utils import class_weight
import os
import binascii
import uuid
import model.base as database
def get_compiled_model(headers,targetGroup):
  feature_columns = []
  for header in headers:
      feature_columns.append(feature_column.numeric_column(header))
  feature_layer = tf.keras.layers.DenseFeatures(feature_columns)
  model = keras.Sequential([
    # keras.layers.Dense(64, activation='relu',input_dim=len(headers)),
    keras.layers.Dense(64, activation='relu',input_dim=len(headers)),
    keras.layers.Dense(64, activation='relu'),
    # keras.layers.Dense(len(headers), activation='relu'),
    keras.layers.Dense(1)
  ])
  optimizer = tf.keras.optimizers.RMSprop(0.001)
  model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])
  return model

def plot_learning_curves(history):
    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch
        # 解决中文乱码问题
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus']=False
    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Mean Abs Error [Value]')
    plt.plot(hist['epoch'], hist['mae'],
            label='Train Error')
    plt.plot(hist['epoch'], hist['val_mae'],
            label = 'Val Error')
    plt.ylim([0,5])
    plt.legend()
    urlstr = str(uuid.uuid1())
    plt.savefig('./static/'+urlstr+'.jpg')
    return urlstr
learning_rate=0.1
def getGroup(x,groupmap):
    return groupmap[str(x)]
def onegrounp(df, column,groupmap):
    df[column] = df[column].apply(lambda x: getGroup(x,groupmap))
def onehot(df, column,max,min):
    dis = max - min
    df[column] = df[column].apply(lambda x: abs((x - min)/dis))
def df_to_dataset(dataframe,target,shuffle=True, batch_size=32):
  dataframe = dataframe.copy()
  labels = dataframe.pop(target)
  print(labels)
  ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
  if shuffle:
    ds = ds.shuffle(buffer_size=len(dataframe))
  ds = ds.batch(batch_size)
  return ds

def norm(x,train_stats):
    return (x - train_stats['mean']) / train_stats['std']

def train(data,socketio):
    df = pd.read_csv(data["filePath"])
    count = len(df)
    train_sum = round(count*0.8)
    test_count = round(count*0.2)
    train_count = round(train_sum*0.8)
    dtypes = df.dtypes
    headers = []
    onehots = {}
    targetGroup = []
    for i in dtypes.keys():
      dtype = str(dtypes[i])
      name = str(i)
      if name != data['target']:
         headers.append(name)
      if dtype == "object" and name != data['target']:
         dataframe = df.copy()
         groupby = dataframe.groupby(name)
         groupDict = dict(list(groupby))
         count = 1
         grupMap = {}
         maxvalue = len(groupDict.keys())
         minvalue = 1
         dis = maxvalue - minvalue
         for k in groupDict.keys():
            grupMap[str(k)] = abs((count - minvalue)/dis)
         onegrounp(df,name,grupMap)
         onehots[name] = {}
         onehots[name]['name'] = name
         onehots[name]['grupMap'] = grupMap
         onehots[name]['maxValue'] = float(maxvalue)
         onehots[name]['minValue'] = float(minvalue)
      if dtype != "object" and name != data['target']:
         dataframe = df.copy()
         groupby = dataframe.groupby(name)
         groupDict = dict(list(groupby))
         count = 1
         grupMap = {}
         maxvalue = df[name].max()
         minvalue = df[name].min()
         onehot(df,name,maxvalue,minvalue)
         onehots[name] = {}
         onehots[name]['name'] = name
         onehots[name]['grupMap'] = grupMap
         onehots[name]['maxValue'] = float(maxvalue) 
         onehots[name]['minValue'] = float(minvalue) 
        #  onehot(df,name,maxvalue,minvalue)
    train_dataset = df.sample(frac=0.8,random_state=0) #分割80%训练集，取不重复的数据
    # train_dataset = df.sample(frac=0.8) #分割80%训练集，取不重复的数据
    test_dataset = df.drop(train_dataset.index)
    train_stats = train_dataset.describe() #查看数据统计的参数值
    train_stats.pop(data['target']) #删除燃油效率特征，因为是标签
    train_stats = train_stats.transpose() #行列转置显示


    train_labels = train_dataset.pop(data['target']) #从数据集删除并保存成变量作为标签
    test_labels = test_dataset.pop(data['target'])

    # normed_train_data = norm(train_dataset,train_stats) #对训练集进行归一化
    # normed_test_data = norm(test_dataset,train_stats) #对测试集进行归一化

    normed_train_data = train_dataset #对训练集进行归一化
    normed_test_data = test_dataset #对测试集进行归一化

    model = get_compiled_model(headers,targetGroup)
    logdir = './dnn-selu-dropout-callbacks/'+ str(data["id"])+"/"+str(data["trainName"])
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    output_model_file = os.path.join(logdir,
                                 "fashion_mnist_model.h5")

    callbacks = [
      keras.callbacks.TensorBoard(logdir),
      keras.callbacks.ModelCheckpoint(output_model_file,
                                      save_best_only = True,
                                      save_Weights_only = False,
                                      ),
      keras.callbacks.EarlyStopping(
        monitor='val_loss', 
        patience=100
      #   monitor='val_auc', 
      #   verbose=1,
      #   patience=100,
      #   mode='max',
      #   restore_best_weights=True
      )
    ]
    # history = model.fit(normed_train_data,
    #         epochs=int(data["times"]),
    #         validation_data=v,
    #         batch_size= round(train_count/10),
    #         callbacks=callbacks)
    # print(normed_train_data)
    # print(normed_train_data)
    history = model.fit(
        normed_train_data, 
        train_labels,
        epochs=int(data["times"]), 
        # epochs=4, 
        validation_split = 0.2, 
        callbacks=callbacks,
        verbose=2)
    urlstr = plot_learning_curves(history)
    model.save(logdir)
    model.load_weights(output_model_file)
    # loss, accuracy = model.evaluate(test_ds)
    # loss, mae, mse = model.evaluate(test_ds)
    # test_predictions = model.predict(normed_test_data).flatten()
    # plt.scatter(test_labels, test_predictions)
    # plt.xlabel('True Values [MPG]')
    # plt.ylabel('Predictions [MPG]')
    # #plt.axis('equal')
    # plt.axis('square') # 正方形，即ｘ轴和ｙ轴比例相同
    # plt.xlim([0,plt.xlim()[1]])
    # plt.ylim([0,plt.ylim()[1]])
    # _ = plt.plot([0, 100], [0, 100]) # 参考的对角线
    # # plt.show()
    # plt.savefig('1.jpg')
    loss, mae, mse = model.evaluate(normed_test_data, test_labels, verbose=2) #测试
    print("Testing set Mean Abs Error: {:5.2f} ".format(mae))
    res = {}
    print(onehots)
    res["onehots"] = onehots
    res["group"] = targetGroup
    res["test"] = {
      "accuracy":mae,
      "loss":loss
    }
    res["imgUrl"] ="http://127.0.0.1:9567/"+urlstr+".jpg"
    trainObj = {
      "trainConfig":{
        "trainMes":res,
        "form":data
      },
      "dataId":data["dataId"],
      "loss":loss,
      "trainName":data["trainName"],
      "accuracy":mae,
      "dataName":data["dataName"]
    }
    messageObj = {
      "trainConfig":{
        "trainMes":res,
        "form":data
      }
    }
    database.createTrain(trainObj)
    database.createMessage(messageObj)
    socketio.emit('train','',namespace='/mes')

def getParam(data):
    df = pd.read_csv(data["filePath"],header=0,nrows=1)
    dtypes = df.dtypes
    res = {
      'param':{},
      "target":''
    }
    k = 0
    for i in dtypes.keys():
      if str(i) != data["target"]:
        res['param'][str(i)] = df.values[0][k]
        k = k + 1
      else:
        res['target'] = df.values[0][k]
    return res
# 预训练数据
def preTrain(data):
    form = data["form"]
    preData = data["preData"]
    trainData =  data["trainData"]
    group = trainData["group"]
    logdir = './dnn-selu-dropout-callbacks/'+ str(form["id"])+"/"+str(form["trainName"])
    output_model_file = os.path.join(logdir,
                                 "fashion_mnist_model.h5")
    model = tf.keras.models.load_model(output_model_file)
    # model.load_weights(output_model_file)
    df = pd.read_csv(form["filePath"],header=0,nrows=1)
    dtypes = df.dtypes
    res = []
    for i in dtypes.keys():
      typeString = str(dtypes[i])
      name = str(i)
      if name != form['target']:
        if 'int' in str(dtypes[i]) or  'float' in str(dtypes[i]):
          if trainData['onehots'][name]['maxValue'] < float(preData[name]):
             res.append(float(1))
          if trainData['onehots'][name]['minValue'] > float(preData[name]):
             res.append(float(0)) 
          if trainData['onehots'][name]['maxValue'] >= float(preData[name]) and trainData['onehots'][name]['minValue'] <= float(preData[name]): 
             dis = trainData['onehots'][name]['maxValue'] - trainData['onehots'][name]['minValue']
             res.append((preData[name] - trainData['onehots'][name]['minValue'])/dis) 
        else:
          if preData[name] in trainData['onehots'][name]["grupMap"].keys():
             res.append(trainData['onehots'][name]["grupMap"][preData[name]])
          else:
             res.append(0.0)
    predictions = model.predict(np.array([(res)]))
    print(predictions)
    # index = np.argmax(predictions[0])
    # print(np.argmax(predictions[0]))
    # print(group[index])
    # print(predictions)
    # print("Predicted survival: {:.2%}".format(predictions[0][0]))
    return  float(predictions[0][0]) 
    # return group[index]
# 预训练数据
def trainOnline(data):
    modelId = data["modelId"]
    preData = data["trainData"]
    modelObj = database.queryModelById(modelId)
    form =json.loads(modelObj["formConfig"])
    trainData =json.loads(modelObj["modelConfig"])
    logdir = './dnn-selu-dropout-callbacks/'+ str(form["id"])+"/"+str(form["trainName"])
    output_model_file = os.path.join(logdir,
                                 "fashion_mnist_model.h5")
    model = tf.keras.models.load_model(output_model_file)
    # model.load_weights(output_model_file)
    df = pd.read_csv(form["filePath"],header=0,nrows=1)
    dtypes = df.dtypes
    res = []
    for i in dtypes.keys():
      typeString = str(dtypes[i])
      name = str(i)
      if name != form['target']:
        if 'int' in str(dtypes[i]) or  'float' in str(dtypes[i]):
          res.append(float(preData[name]))
        if str(dtypes[i]) =="object":
          for onehot in trainData['onehots']:
              if onehot['name'] == name:
                  if preData[name] in onehot["grupMap"].keys():
                    res.append(onehot["grupMap"][preData[name]])
                  else:
                    res.append(0.0)
    print(res)
    predictions = model.predict(np.array([(res)]))
    print(predictions)
    print("Predicted survival: {:.2%}".format(predictions[0][0]))
    return "{:.2%}".format(predictions[0][0])
