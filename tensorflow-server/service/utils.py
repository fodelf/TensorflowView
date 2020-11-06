import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from tensorflow import keras
import os
def get_compiled_model():
  # model = tf.keras.Sequential([
  #   tf.keras.layers.Dense(10, activation='relu'),
  #   tf.keras.layers.Dense(10, activation='relu'),
  #   tf.keras.layers.Dense(1, activation='sigmoid')
  # ])
  # model.compile(optimizer='adam',
  #               loss='binary_crossentropy',
  #               metrics=['accuracy'])
  model = keras.models.Sequential()
  for _ in range(20):
    model.add(keras.layers.Dense(10, activation="relu"))
  # model.add(keras.layers.AlphaDropout(rate=0.5))
    # AlphaDropout: 1. 均值和方差不变 2. 归一化性质也不变
  model.add(keras.layers.Dense(1, activation="sigmoid"))
  model.compile(optimizer='adam',
                loss='binary_crossentropy',
                metrics=['accuracy'])
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

def train(data):
    df = pd.read_csv(data["filePath"])
    df2 = pd.read_csv(data["filePath"])
    df2['thal'] = df2['thal'].astype("category")
    df2['thal'] = df2.thal.cat.codes
    print(df2['thal'])
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    data1 = {
        'thal':['fixed']
    }
    df1 = pd.DataFrame(data1,
               columns=['thal'])
    df1['thal'] = df1['thal'].astype("category")
    df1['thal'] = df1['thal'].cat.codes
    print(df1['thal'])
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    dtypes = df.dtypes
    for i in dtypes.keys():
      dtype = str(dtypes[i])
      if dtype == "object":
         key = str(i)
         df[key] = pd.Categorical(df[key])
         df[key] = df[key].cat.codes
    target = df.pop(data['target'])
    dataset = tf.data.Dataset.from_tensor_slices((df.values, target.values))
    train_dataset = dataset.shuffle(len(df)).batch(1)
    model = get_compiled_model()
    logdir = './dnn-selu-dropout-callbacks'
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    output_model_file = os.path.join(logdir,
                                    "fashion_mnist_model.h5")
    callbacks = [
        keras.callbacks.TensorBoard(logdir),
        keras.callbacks.ModelCheckpoint(output_model_file,
                                        save_best_only = True),
        keras.callbacks.EarlyStopping(patience=5, min_delta=1e-3)
    ]
    history = model.fit(train_dataset, epochs=10,callbacks=callbacks)
    plot_learning_curves(history)

def parseHeader(filePath):
    df = pd.read_csv(filePath,header=0,nrows=1)
    # print(df.dtypes)
    # print(df.info()["Data"])
    info = df.info()
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