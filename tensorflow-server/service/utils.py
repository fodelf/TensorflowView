import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from tensorflow import keras
import json
# from keras.backend import K
# from keras.callbacks import LearningRateScheduler
from tensorflow.keras.callbacks import LearningRateScheduler
from tensorflow import feature_column
from sklearn.model_selection import train_test_split
import os
import binascii
import uuid
import model.database as database
def get_compiled_model(headers):
  # model = tf.keras.Sequential([
  #   tf.keras.layers.Dense(10, activation='relu'),
  #   tf.keras.layers.Dense(10, activation='relu'),
  #   tf.keras.layers.Dense(1, activation='sigmoid')
  # ])
  # model.compile(optimizer='adam',
  #               loss='binary_crossentropy',
  #               metrics=['accuracy'])
  # model = keras.models.Sequential()
  # for _ in range(20):
  #   model.add(keras.layers.Dense(10, activation="relu"))
  # # model.add(keras.layers.AlphaDropout(rate=0.5))
  #   # AlphaDropout: 1. 均值和方差不变 2. 归一化性质也不变
  # model.add(keras.layers.Dense(1, activation="sigmoid"))
  feature_columns = []
  for header in headers:
      feature_columns.append(feature_column.numeric_column(header))
  feature_layer = tf.keras.layers.DenseFeatures(feature_columns)
  model = keras.models.Sequential()
  # model.add(keras.layers.Flatten(input_shape=(0,1, len(headers))),)
  # model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(,  return_sequences=True)))
  for _ in range(20):
    # model.add(keras.layers.Dense(10, activation="selu"))
    model.add(keras.layers.Dense(len(headers), activation="relu"))
    # model.add(keras.layers.Dense(10, activation="relu"))
  model.add(keras.layers.AlphaDropout(rate=0.5))
    # AlphaDropout: 1. 均值和方差不变 2. 归一化性质也不变
  model.add(keras.layers.Dense(1, activation="sigmoid"))
  # model = tf.keras.Sequential([
  #   feature_layer,
  #   keras.layers.Dense(128, activation='relu'),
  #   keras.layers.Dense(128, activation='relu'),
  #   keras.layers.Dense(1, activation='sigmoid')
  # ])
  model.compile(
                optimizer='adam',
                loss='binary_crossentropy',
                metrics=['accuracy'],
                run_eagerly=True,
                # optimizer='sgd'
                )
  # model.compile(optimizer='adam',
  #             loss='binary_crossentropy',
  #             metrics=['accuracy'],
  #             run_eagerly=True)
  return model

def plot_learning_curves(history):
    pd.DataFrame(history.history).plot(figsize=(8, 5))
    plt.grid(True)
    plt.gca().set_ylim(0, 1)
    # plt.show()
    urlstr = str(uuid.uuid1())
    plt.savefig('./static/'+urlstr+'.jpg')
    return urlstr
# predictions = model.predict(np.array([(63,1,1,145,233,1,2,150,0,2.3,3,0,2)]))
# predictions = model.predict(np.array([(67,1,4,160,286,0,2,108,1,1.5,2,3,3)]))
# print(predictions)
# print("Predicted survival: {:.2%}".format(predictions[0][0]))
# print(predictions)
# def scheduler(epoch):
#     # 每隔100个epoch，学习率减小为原来的1/10
#     if epoch % 10 == 0 and epoch != 0:
#         lr = K.get_value(model.optimizer.lr)
#         K.set_value(model.optimizer.lr, lr * 0.1)
#         print("lr changed to {}".format(lr * 0.1))
#     return K.get_value(model.optimizer.lr)
 
# reduce_lr = LearningRateScheduler(scheduler)

# num_epochs = 100
learning_rate=0.1
#定义学习率衰减函数
def scheduler(epoch):
   
    # if epoch % 5 == 0 and epoch != 0:
    #     return learning_rate * 0.1
    return 0.0001
def num(x):
    num = str(x).encode('utf-8')
    str_16 = binascii.b2a_hex(num)
    print(int(str_16, 16))
    return int(str_16, 16)
def getGroup(x,groupmap):
    # print(x)
    # print("xxxxxxxxxxxxxxxxxx")
    return groupmap[str(x)]
def onegrounp(df, column,groupmap):
    # df[column] = df[column].apply(lambda x: abs(hash(str(x))))
    # df[column] = df[column].apply(lambda x: binascii.b2a_hex(x))
    df[column] = df[column].apply(lambda x: getGroup(x,groupmap))
def onehot_hash(df, column):
    # df[column] = df[column].apply(lambda x: abs(hash(str(x))))
    # df[column] = df[column].apply(lambda x: binascii.b2a_hex(x))
    df[column] = df[column].apply(lambda x: num(x))
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

def train(data,socketio):
    df = pd.read_csv(data["filePath"])
    count = len(df)
    train_sum = round(count*0.8)
    test_count = round(count*0.2)
    train_count = round(train_sum*0.8)
    dtypes = df.dtypes
    headers = []
    onehots = []
    for i in dtypes.keys():
      dtype = str(dtypes[i])
      name = str(i)
      if name != data['target']:
         headers.append(name)
      if dtype == "object":
         key = str(i)
         dataframe = df.copy()
         groupby = dataframe.groupby(key)
         groupDict = dict(list(groupby))
         count = 1
         grupMap = {}
         for k in groupDict.keys():
            # if str(k) !='1' and str(k) !='2':
            # grupMap[str(k)] = np.asarray([0,0,1]).astype(np.float32)
            # grupMap[str(k)] = np.a([0,0,1]).astype(np.float32)
            grupMap[str(k)] = count
            count = count+1

         print(grupMap)
         child = {}
         child['name'] = key
         child['grupMap'] = grupMap
         onegrounp(df,key,grupMap)
        #  onehot_hash(df,key)
         maxvalue = df[key].max()
         minvalue = df[key].min()
         onehot(df,key,maxvalue,minvalue)
         child['max'] = str(maxvalue)
         child['min'] = str(minvalue)
         onehots.append(child)
         print(df[key])
    # return ""
    # df.to_csv('out.csv')
    # train = pd.read_csv('out.csv',header=0, skiprows=3,nrows= train_count)
    # test = pd.read_csv('out.csv',header=0,skiprows= train_sum,nrows=count)
    # val = pd.read_csv('out.csv',header=0,,skiprows= train_sum,nrows=train_count)
    train, test = train_test_split(df, test_size=0.2)
    train, val = train_test_split(train, test_size=0.2)
    target = train.pop(data['target'])
    train_dataset = tf.data.Dataset.from_tensor_slices((train.values, target.values))
    target = test.pop(data['target'])
    test_dataset = tf.data.Dataset.from_tensor_slices((test.values,target.values))
    target = val.pop(data['target'])
    val_dataset = tf.data.Dataset.from_tensor_slices((val.values, target.values))
    batch_size = 1
    train_ds = train_dataset.shuffle(len(train)).batch(batch_size)
    test_ds = test_dataset.shuffle(len(test)).batch(batch_size)
    val_ds = val_dataset.shuffle(len(val)).batch(batch_size)
    model = get_compiled_model(headers)
    logdir = './dnn-selu-dropout-callbacks/'+ str(data["id"])+"/"+str(data["trainName"])
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    # output_model_file = os.path.join(logdir,
    #                                 "fashion_mnist_model.h5")
    # output_model_file = os.path.join(logdir,
    #                                 "cp.ckpt")
    # callbacks = [
    #     keras.callbacks.TensorBoard(logdir),
    #     tf.keras.callbacks.ModelCheckpoint(filepath=output_model_file,
    #                                              save_weights_only=True,
    #                                              verbose=1)
    #     # keras.callbacks.ModelCheckpoint(output_model_file,
    #     #                                 save_best_only = True),
    #     # keras.callbacks.EarlyStopping(patience=5, min_delta=1e-3)
    # ]
    output_model_file = os.path.join(logdir,
                                 "fashion_mnist_model.h5")

    callbacks = [
      keras.callbacks.TensorBoard(logdir),
      keras.callbacks.ModelCheckpoint(output_model_file,
                                      save_best_only = True,
                                      save_Weights_only = False,
                                      ),
      # keras.callbacks.EarlyStopping(patience=5, min_delta=1e-3),
      # keras.callbacks.LearningRateScheduler(scheduler),
      keras.callbacks.EarlyStopping(
          # patience=5, 
          # min_delta=1e-3,
          monitor='val_loss',
          min_delta=0,
          patience=10,
          verbose=1
      )
    ]
    history = model.fit(train_ds, 
            epochs=int(data["times"]),
            validation_data=val_ds,
            # verbose=1,
            batch_size= round(train_count/10),
            callbacks=callbacks)
    urlstr = plot_learning_curves(history)
    # model.load_weights(logdir)
    # tf.saved_model.save(model, logdir)
    model.save(logdir)
    # imported = tf.saved_model.load(logdir)
    # outputs = imported(model)
    model.load_weights(output_model_file)
    loss, accuracy = model.evaluate(test_ds)
    # predictions = model.predict(test_ds)
    # 显示部分结果
    # for prediction, survived in zip(predictions[:2], list(test_ds)[0][1][:2]):
    #   print("Predicted survival: {:.2%}".format(prediction[0]),
    #         " | Actual outcome: ",
    #         ("SURVIVED" if bool(survived) else "DIED"))
    # data1 = [67,1,4,160,286,0,2,108,1,1.5,2,3,0.514844]
    # df1= pd.DataFrame(data1)
    # print(df1)
    # print("ssssssssssssssssssssssssssssssssssssssssss")      
    # labels = ["age","sex","cp","trestbps",
    #            "chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"]
    # print(labels)   
    # predictions = model.predict(tf.data.Dataset.from_tensor_slices((np.array([67,1,4,160,286,0,2,108,1,1.5,2,3,0.514844]),
    # df = pd.read_csv("./static/2.csv",header=0,nrows=1)
    # predictions = model.predict(tf.data.Dataset.from_tensor_slices(df))
    # print(tf.data.Dataset.from_tensor_slices((dict(df1))))
    # predictions = model.predict(x=df1)
    # predictions = model.predict(np.array([(63,1,1,145,233,1,2,150,0,2.3,3,0,0.50)]))
    # print(predictions)
    # print("Predicted survival: {:.2%}".format(predictions[0][0]))
    # print("xxxxxxxxxxxxxxxxxx")
    res = {}
    res["onehots"] = onehots
    res["test"] = {
      "accuracy":accuracy,
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
      "accuracy":accuracy
    }
    messageObj = {
      "trainConfig":{
        "trainMes":res,
        "form":data
      }
    }
    database.createTrain(trainObj)
    database.createMessage(messageObj)
    # service.socketio.test_message(res)
    socketio.emit('train','',namespace='/mes')
    # return res

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

def parseHeader(filePath):
    df = pd.read_csv(filePath,header=0,nrows=1)
    # print(df.dtypes)
    # print(df.info()["Data"])
    # info = df.info()
    print(df.values[0])
    dtypes = df.dtypes
    res = []
    k = 0
    for i in dtypes.keys():
      child = {}
      typeString = str(dtypes[i])
      if 'int' in str(dtypes[i]) or  'float' in str(dtypes[i]):
          typeString ='数值'
      if str(dtypes[i]) =="object":
          typeString ='文本'
      child['name'] = str(i)
      child['code'] = k
      child['type'] = typeString
      child[str(k)] = df.values[0][k]
      k = k + 1
      res.append(child)
    return res

def test(data):
    logdir = './dnn-selu-dropout-callbacks'
    model = tf.keras.models.load_model(logdir)
    predictions = model.predict(np.array([(63,0,4,150,407,0,2,154,0,4,2,3,1.0)]))
    # new_model.summary()
    # dis = max - min
    # df[column] = df[column].apply(lambda x: abs((x - min)/dis))  
    # predictions = new_model.predict(np.array([(67,1,4,160,286,0,2,108,1,1.5,2,3,0.514844)]))
    print(predictions)
    print("Predicted survival: {:.2%}".format(predictions[0][0]))
    return ""
# 预训练数据
def preTrain(data):
    form = data["form"]
    preData = data["preData"]
    trainData =  data["trainData"]
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
          print(preData[name])
        if str(dtypes[i]) =="object":
          for onehot in trainData['onehots']:
              if onehot['name'] == name:
                  if preData[name] in onehot["grupMap"].keys():
                    res.append(onehot["grupMap"][preData[name]])
                  else:
                    res.append(0.0)
    predictions = model.predict(np.array([(res)]))
    print(predictions)
    print("Predicted survival: {:.2%}".format(predictions[0][0]))
    return "{:.2%}".format(predictions[0][0])

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
          print(preData[name])
        if str(dtypes[i]) =="object":
          for onehot in trainData['onehots']:
              if onehot['name'] == name:
                  if preData[name] in onehot["grupMap"].keys():
                    res.append(onehot["grupMap"][preData[name]])
                  else:
                    res.append(0.0)
    predictions = model.predict(np.array([(res)]))
    print(predictions)
    print("Predicted survival: {:.2%}".format(predictions[0][0]))
    return "{:.2%}".format(predictions[0][0])
