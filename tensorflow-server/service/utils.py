import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow import feature_column
from sklearn.model_selection import train_test_split
import os
import binascii
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
  # model.add(feature_layer)
  for _ in range(20):
    model.add(keras.layers.Dense(10, activation="relu"))
  model.add(keras.layers.AlphaDropout(rate=0.5))
    # AlphaDropout: 1. 均值和方差不变 2. 归一化性质也不变
  model.add(keras.layers.Dense(1, activation="sigmoid"))
  # model = tf.keras.Sequential([
  #   feature_layer,
  #   keras.layers.Dense(128, activation='relu'),
  #   keras.layers.Dense(128, activation='relu'),
  #   keras.layers.Dense(1, activation='sigmoid')
  # ])
  model.compile(optimizer='adam',
                loss='binary_crossentropy',
                metrics=['accuracy'],
                # run_eagerly=True
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
    plt.savefig('./static/1.jpg')
# predictions = model.predict(np.array([(63,1,1,145,233,1,2,150,0,2.3,3,0,2)]))
# predictions = model.predict(np.array([(67,1,4,160,286,0,2,108,1,1.5,2,3,3)]))
# print(predictions)
# print("Predicted survival: {:.2%}".format(predictions[0][0]))
# print(predictions)
def num(x):
    num = str(x).encode('utf-8')
    str_16 = binascii.b2a_hex(num)
    print(int(str_16, 16))
    return int(str_16, 16)

def onegrounp(df, column,groupmap):
    # df[column] = df[column].apply(lambda x: abs(hash(str(x))))
    # df[column] = df[column].apply(lambda x: binascii.b2a_hex(x))
    df[column] = df[column].apply(lambda x: groupmap[str(x)])    
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
def train(data):
    df = pd.read_csv(data["filePath"])
    # df2 = pd.read_csv(data["filePath"])
    # onehot_hash(df2,'thal')
    # df2['thal'] = df2['thal'].astype("category")
    # df2['thal'] = df2.thal.cat.codes
    # print(df2['thal'])
    # print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    # data1 = {
    #     'thal':['fixed']
    # }
    # df1 = pd.DataFrame(data1,
    #            columns=['thal'])
    # onehot_hash(df1,'thal')           
    # print(df1['thal'])
    # print(abs(hash(str('fixed')))%D)
    # return("sssss")  
    # print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
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
         groupby = df.groupby(key)
         groupDict = dict(list(groupby))
         count = 1 
         grupMap = {}
         for k in groupDict.keys():
            grupMap[str(k)] = count
            count = count+1
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
    target = df.pop(data['target'])
    dataset = tf.data.Dataset.from_tensor_slices((df.values, target.values))
    # train_dataset = dataset.shuffle(len(df)).batch(1)
    count = len(df)
    train_num = round(count*0.8)
    test_count = round(count*0.2)
    train_ds = dataset.shuffle(train_num).batch(1)
    test_ds = dataset.shuffle(test_count).batch(1)
    val_ds = dataset.shuffle(test_count).batch(1)       
        #  df[key] = pd.Categorical(df[key])
        #  df[key] = df[key].cat.codes
    # target = df.pop(data['target'])
    # train, test = train_test_split(df, test_size=0.2)
    # train, val = train_test_split(train, test_size=0.2)
    # batch_size = 5 # 小批量大小用于演示
    # train_ds = df_to_dataset(train,data['target'],batch_size=batch_size)
    # val_ds = df_to_dataset(val,data['target'],shuffle=False, batch_size=batch_size)
    # test_ds = df_to_dataset(test,data['target'],shuffle=False, batch_size=batch_size)
    # dataset = tf.data.Dataset.from_tensor_slices((df.values, target.values))
    # train_df, test = train_test_split(df, test_size=0.2)
    # train_dataset  = tf.data.Dataset.from_tensor_slices((train_df.values, target.values))
    # train_dataset, val_dataset = train_test_split(train_dataset, test_size=0.2)
    # train_dataset = dataset.shuffle(int(len(df))).batch(1)
    # val_dataset =  dataset.shuffle(int(len(df)**0.2)).batch(1)
    # test_dataset = dataset.shuffle(int(len(df)**0.4)).batch(1)
    # val_dataset = dataset.shuffle(len(df)**0.4).batch(1).repeat()
    model = get_compiled_model(headers)
    logdir = './dnn-selu-dropout-callbacks'
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
      keras.callbacks.EarlyStopping(patience=5, min_delta=1e-3),
    ]
    history = model.fit(train_ds, 
            epochs=100,
            validation_data=val_ds,
            callbacks=callbacks)
    plot_learning_curves(history)
    # model.load_weights(logdir)
    # tf.saved_model.save(model, logdir)
    model.save(logdir)
    # imported = tf.saved_model.load(logdir)
    # outputs = imported(model)
    model.load_weights(output_model_file)
    loss, accuracy = model.evaluate(test_ds)
    data1 = {
        "age":[67],
        "sex":[1],
        "cp":[4],
        "trestbps":[4],
        "chol":[4],
        "fbs":[4],
        "restecg":[4],
        "thalach":[4],
        "exang":[4],
        "oldpeak":[4],
        "slope":[4],
        "ca":[4],
        'thal':[0.514844]
    }
    # data1 = [67,1,4,160,286,0,2,108,1,1.5,2,3,0.514844]
    df1= pd.DataFrame(data1)
    # print(df1)
    print("ssssssssssssssssssssssssssssssssssssssssss")      
    # labels = ["age","sex","cp","trestbps",
    #            "chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"]
    # print(labels)   
    # predictions = model.predict(tf.data.Dataset.from_tensor_slices((np.array([67,1,4,160,286,0,2,108,1,1.5,2,3,0.514844]),
    #  np.array(["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"]))))
      # np.array([(67)]), np.array((1])),
      # np.array([4]), np.array([160]),
      # np.array([286]), np.array([0]),
      # np.array([2]), np.array([108]),
      # np.array([1]), np.array([1.5]),
      # np.array([2]), np.array([3]),
      # np.array([0.514844])
      # ])
    # df = pd.read_csv("./static/2.csv",header=0,nrows=1)
    # predictions = model.predict(tf.data.Dataset.from_tensor_slices(df))
    # print(tf.data.Dataset.from_tensor_slices((dict(df1))))
    # predictions = model.predict(x=df1)
    predictions = model.predict(np.array([(63,1,1,145,233,1,2,150,0,2.3,3,0,0.50)]))
    print(predictions)
    print("Predicted survival: {:.2%}".format(predictions[0][0]))
    print("xxxxxxxxxxxxxxxxxx")
    res = {}
    res["onehots"] = onehots
    res["test"] = {
      "accuracy":accuracy,
      "loss":loss
    }
    res["imgUrl"] ="http://127.0.0.1:9567/1.jpg"
    print("Accuracy", accuracy)    
    print("loss", loss)
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