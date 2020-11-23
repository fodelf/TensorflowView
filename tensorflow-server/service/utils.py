import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from tensorflow import keras
import json
import tempfile
# from keras.backend import K
# from keras.callbacks import LearningRateScheduler
from tensorflow.keras.callbacks import LearningRateScheduler
from tensorflow import feature_column
from sklearn.model_selection import train_test_split
from sklearn.utils import class_weight
import os
import binascii
import uuid
import model.base as database
def get_compiled_model(headers,targetGroup,denseNum):
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
  # for _ in range(20):
  #   model.add(keras.layers.Dense(len(headers), activation='relu'))
    # model.add(keras.layers.Dense(10))
  #   # model.add(keras.layers.Dense(10, activation="selu"))
  #   # model.add(keras.layers.Dense(len(headers), activation="relu"))
    # model.add(keras.layers.Dense(len(headers), activation="relu"))
    # model.add(keras.layers.AlphaDropout(rate=0.5))
    # model.add(keras.layers.Dense(10, activation="relu"))
  # model.add(tf.keras.layers.Dense(128,activation='relu'))
  # model.add(tf.keras.layers.Flatten())
    # AlphaDropout: 1. 均值和方差不变 2. 归一化性质也不变
  # model.add(keras.layers.Dense(len(headers), activation='relu'))
  # model.add(keras.layers.Dense(3))
  if len(targetGroup) > 2:
    print('222222222222222222222222222222222222222222')
    denseCount =len(targetGroup)
    # model.add(keras.layers.Dense(denseCount, activation="softmax"))
    # model.add(keras.layers.Flatten())
    # model.add(keras.layers.Dense(len(headers), activation='relu'))
    # model.add(keras.layers.Dense(len(headers), activation='relu'))
    # model.add(keras.layers.Flatten())
    # model.add(keras.layers.Dense(len(headers), activation='relu'))
    # for _ in range(2):
    #   model.add(keras.layers.Dense(10*len(headers), activation='relu'))
    # for _ in range(2):
    #   model.add(keras.layers.Dense(5*len(headers), activation='relu'))
    # model.add(keras.layers.Dense(10*len(headers), activation='relu'))
    # for _ in range(denseNum):
    #   model.add(keras.layers.Dense(len(headers), activation='relu'))
      
    # # model.add(keras.layers.Dense(len(headers), activation='relu'))
    # model.add(keras.layers.AlphaDropout(rate=0.5))
    # # model.add(keras.layers.Dense(denseCount))
    # model.add(tf.keras.layers.Dense(denseCount, activation='softmax'))
    # model.add(tf.keras.layers.Dense(denseCount))
    # model.compile(optimizer='adam',
    #           loss='sparse_categorical_crossentropy',
    #           metrics=['accuracy'])
    # model.compile(optimizer= tf.keras.optimizers.Adam(),
    #               loss= tf.keras.losses.SparseCategoricalCrossentropy(),
    #              metrics=['accuracy'])
    model = keras.Sequential([
      # keras.layers.Dense(64, activation='relu',input_dim=len(headers)),
      keras.layers.Dense(64, activation='relu',input_dim=len(headers)),
      keras.layers.Dense(64, activation='relu'),
      keras.layers.AlphaDropout(rate=0.5),
      # keras.layers.Dense(len(headers), activation='relu'),
      keras.layers.Dense(denseCount, activation='softmax')
    ])
    model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
    # model.compile(optimizer=keras.optimizers.Adam(lr=1e-3),
    #               loss=keras.losses.BinaryCrossentropy(),
    #              metrics=[keras.metrics.SparseCategoricalAccuracy()])
    # model.add(tf.keras.layers.Dense(denseCount))
    # model.add(tf.keras.layers.Dense(denseCount))
    # model.add(tf.keras.layers.Dense(denseCount))
    # model.compile(optimizer='adam',
    #              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    #              metrics=["accuracy"])
    # model.compile(optimizer= tf.keras.optimizers.Adam(lr=1e-3),
    #               loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    #             metrics=["accuracy"])
    # model.compile( optimizer=keras.optimizers.Adam(lr=1e-3),
    #               loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    #             metrics=["accuracy"])
    # model.compile(optimizer=tf.keras.optimizers.Adam(),
    #           loss='sparse_categorical_crossentropy',
    #           metrics=["accuracy"])
    # model.add(keras.layers.Dense(denseCount))
    # model.compile(optimizer='adam',
    #           loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    #           metrics=['accuracy'])
  else:
    # for _ in range(denseNum):
    #   model.add(keras.layers.Dense(len(headers), activation='relu'))
    #   # model.add(keras.layers.Dense(10, activation='relu'))
    # # model.add(keras.layers.Dense(len(headers), activation='relu'))
    # # model.add(keras.layers.Dense(len(headers), activation='relu'))
    # # model.add(keras.layers.Dense(len(headers), activation='relu'))
    # model.add(keras.layers.AlphaDropout(rate=0.5))
    # model.add(keras.layers.Dense(1, activation="sigmoid"))
    model = keras.Sequential([
      # keras.layers.Dense(64, activation='relu',input_dim=len(headers)),
      keras.layers.Dense(64, activation='relu',input_dim=len(headers)),
      keras.layers.Dense(64, activation='relu'),
      keras.layers.AlphaDropout(rate=0.5),
      # keras.layers.Dense(len(headers), activation='relu'),
      keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'],
              run_eagerly=True)
  # model.summary()
    # model.compile(
    #           optimizer='adam',
    #           loss='categorical_crossentropy',
    #           metrics=['accuracy'],
    #           run_eagerly=True,
    #           # optimizer='sgd'
    #           )
  # model.add(keras.layers.Dense(denseCount, activation="sigmoid"))
  # 配置 SGD，学习率为 0.1
  # optimizer = tf.keras.optimizers.SGD(0.1)
  # model.compile(optimizer=optimizer,
  #             loss = loss,
  #             metrics=['accuracy'])

  # model.compile(optimizer = 'adam' , loss = 'sparse_categorical_crossentropy',metrics = ['accuracy'])
  # model = tf.keras.Sequential([
  #   feature_layer,
  #   keras.layers.Dense(128, activation='relu'),
  #   keras.layers.Dense(128, activation='relu'),
  #   keras.layers.Dense(1, activation='sigmoid')
  # ])
#    layer0 = tf.keras.layers.Dense(class_num, input_shape=(x_data.shape[1],), activation='softmax')
#  model = tf.keras.Sequential([layer0])
#  model.compile(loss='categorical_crossentropy', optimizer='adam')
# #首先先将数据集归一化
# train_image = train_image/255
# test_image = test_image/255
# #创建model
# model = tf.keras.Sequential()
# #添加隐含层
# model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
# model.add(tf.keras.layers.Dense(128,activation = 'relu'))
# model.add(tf.keras.layers.Dense(10,activation = 'softmax'))

# #编译model
# model.compile(optimizer = 'adam' , loss = 'sparse_categorical_crossentropy',metrics = ['acc'])
  # model.compile(loss='categorical_crossentropy', optimizer='adam')
# #训练model
# model.fit(train_image , train_label,epochs = 5)
# #进行model的预测
# model.predict(test_image , test_label)

  # model.compile(
  #               optimizer='adam',
  #               loss='categorical_crossentropy',
  #               metrics=['accuracy'],
  #               run_eagerly=True,
  #               # optimizer='sgd'
  #               )
  # model.compile(optimizer=tf.keras.optimizers.RMSprop(),
  #               loss=tf.keras.losses.SparseCategoricalCrossentropy(),
  #               metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])
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
def getGroup(x,groupmap):
    return groupmap[str(x)]
def onegrounp(df, column,groupmap):
    # df[column] = df[column].apply(lambda x: abs(hash(str(x))))
    # df[column] = df[column].apply(lambda x: binascii.b2a_hex(x))
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

def train(data,socketio):
    df = pd.read_csv(data["filePath"])
    totalCount = len(df)
    train_sum = round(totalCount*0.8)
    test_count = round(totalCount*0.2)
    train_count = round(train_sum*0.8)
    dtypes = df.dtypes
    headers = []
    onehots = {}
    targetGroup = []
    class_weight = {}
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
      else:
         key = str(i)
         dataframe = df.copy()
         count = 0
         grupMap = {}
         groupby = dataframe.groupby(name)
         groupDict = dict(list(groupby))
         keysCount = len(groupDict.keys())
         for k in groupDict.keys():
            targetGroup.append(str(k))
            grupMap[str(k)] = count
            class_weight[count] = (1/len(groupDict[k]))*(totalCount)/keysCount
            count = count+1
         onegrounp(df,key,grupMap)
        #  print(df[name])
      # if dtype == "object" and name != data['target']:
      #    dataframe = df.copy()
      #    groupby = dataframe.groupby(name)
      #    groupDict = dict(list(groupby))
      #    count = 1
      #    grupMap = {}
      #    maxvalue = len(groupDict.keys())
      #    minvalue = 1
      #    dis = maxvalue - minvalue
      #    for k in groupDict.keys():
      #       grupMap[str(k)] = abs((count - minvalue)/dis)
      #    onegrounp(df,name,grupMap)
      #    child = {}
      #    child['name'] = name
      #    child['grupMap'] = grupMap
      #    onehots.append(child)
      # if dtype == "object" and name != data['target']:
      #    dataframe = df.copy()
      #    groupby = dataframe.groupby(name)
      #    groupDict = dict(list(groupby))
      #    count = 1
      #    grupMap = {}
      #    for k in groupDict.keys():
      #       grupMap[str(k)] = count
      #       count = count+1
      #    onegrounp(df,name,grupMap)
      #    maxvalue = df[name].max()
      #    minvalue = df[name].min()
      #    count = 0
      #    grupMap = {}
      #    dis = maxvalue - minvalue
      #    for k in groupDict.keys():
      #       grupMap[str(k)] = abs((count - minvalue)/dis) 
      #       count = count+1
      #    child = {}
      #    child['name'] = name
      #    child['grupMap'] = grupMap
      #    onehots.append(child)
      #    onehot(df,name,maxvalue,minvalue)
        #  child['max'] = str(maxvalue)
        #  child['min'] = str(minvalue)
        #  onehots.append(child)
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
    # batch_size = 1
    # batch_size=round(len(train_dataset)/10)
    batch_size = round(train_count/10)
    # print(batch_size)
    train_ds = train_dataset.shuffle(len(train)).batch(batch_size)
    test_ds = test_dataset.shuffle(len(test)).batch(batch_size)
    val_ds = val_dataset.shuffle(len(val)).batch(batch_size)
    # train_ds = train_dataset.shuffle(round(len(train)*0.8)).batch(batch_size)
    # test_ds = test_dataset.shuffle(round(len(test)*0.8)).batch(batch_size)
    # val_ds = val_dataset.shuffle(round(len(val)*0.8)).batch(batch_size)
    model = get_compiled_model(headers,targetGroup,int(data["number"]))
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
      # keras.callbacks.EarlyStopping(patience=5, min_delta=1e-3),
      # keras.callbacks.LearningRateScheduler(scheduler),
      keras.callbacks.EarlyStopping(
        monitor='val_loss',
        min_delta=0,
        patience=100,
        verbose=0,
        baseline=None,
        restore_best_weights=False
          # patience=5,
          # min_delta=1e-3,
          # # monitor='val_loss',
          # monitor='val_loss',
          # min_delta=0.00003,
          # patience=10000,
          # verbose=1,
          # mode='min'
          # # mode="max"
      )
    ]
    # initial_weights = os.path.join(tempfile.mkdtemp(), 'initial_weights')
    # model.save_weights(initial_weights)
    # model.load_weights(initial_weights)
    # class_weight = {0: 5.57, 1: 0.64,2:0.87}
    print(class_weight)
    # class_weight = {0: 0.1, 1: 2,2:1.5}

    # my_class_weight = class_weight.compute_class_weight('balanced',
    #                                              np.unique(train_dataset1),
    #                                              train_dataset1)
    # class_weight_dict = dict(zip([x for x in np.unique(train_dataset1)], my_class_weight))
    history = model.fit(train_ds,
            epochs=int(data["times"]),
            validation_data=val_ds,
            # class_weight = 'auto',
            # verbose=1,
            class_weight=class_weight,
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
    res = {}
    res["onehots"] = onehots
    res["group"] = targetGroup
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
      "accuracy":accuracy,
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
    print(res)
    predictions = model.predict(np.array([(res)]))
    print(predictions)
    index = np.argmax(predictions[0])
    print(np.argmax(predictions[0]))
    print(group[index])
    # print(predictions)
    # print("Predicted survival: {:.2%}".format(predictions[0][0]))
    res = []
    for prediction in predictions:
        resChild = []
        for child in prediction:
          resChild.append(float(child))
        res.append(resChild)
    return res
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
    print(preData)
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
