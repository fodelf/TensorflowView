import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from tensorflow import keras
import os
csv_file = tf.keras.utils.get_file('heart.csv', 'https://storage.googleapis.com/applied-dl/heart.csv')

df = pd.read_csv(csv_file)

df.head()

df.dtypes

df['thal'] = pd.Categorical(df['thal'])
df['thal'] = df.thal.cat.codes
print(df['thal'])
target = df.pop('target')
dataset = tf.data.Dataset.from_tensor_slices((df.values, target.values))
train_dataset = dataset.shuffle(len(df)).batch(1)

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

history = model.fit(train_dataset, epochs=100,callbacks=callbacks)

def plot_learning_curves(history):
    pd.DataFrame(history.history).plot(figsize=(8, 5))
    plt.grid(True)
    plt.gca().set_ylim(0, 1)
    plt.show()
    plt.savefig('1.jpg')

plot_learning_curves(history)

# predictions = model.predict(np.array([(63,1,1,145,233,1,2,150,0,2.3,3,0,2)]))
predictions = model.predict(np.array([(67,1,4,160,286,0,2,108,1,1.5,2,3,3)]))
print(predictions)
print("Predicted survival: {:.2%}".format(predictions[0][0]))
# print(predictions)
