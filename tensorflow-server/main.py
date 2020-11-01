import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sklearn
import pandas as pd
import os
import sys
import time
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from tensorflow import keras

# fashion_mnist = keras.datasets.fashion_mnist
# (x_train_all, y_train_all), (x_test, y_test) = fashion_mnist.load_data()
# x_valid, x_train = x_train_all[:1], x_train_all[1:]
# y_valid, y_train = y_train_all[:1], y_train_all[1:]
x_valid = np.array(
  [
     (1),
     (2),
     (3)
  ]
)
y_valid = np.array(
  [
     (1),
     (2)
  ]
)
x_train = np.array(
  [
(1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3)
  ],
  dtype =  float
)
y_train = np.array(
  [
(1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3)
  ],
  dtype =  float
)
x_test = np.array(
  [
(1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3)
  ],
  dtype =  float
)
y_test = np.array(
  [
(1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3),
     (1),
     (2),
     (3)
  ],
  dtype =  float
)
  
# print(x_valid, y_valid)
print(x_train.shape, y_train.shape)
# print(x_test.shape, y_test.shape)
# print(x_valid.shape, y_valid.shape)
# print(x_train.shape, y_train.shape)
# print(x_test.shape, y_test.shape)

scaler = StandardScaler()
# x_train: [None, 28, 28] -> [None, 784]
x_train_scaled = scaler.fit_transform(
    x_train.astype(np.float).reshape(-1, 1))
x_valid_scaled = scaler.transform(
    x_valid.astype(np).reshape(-1, 1))
x_test_scaled = scaler.transform(
    x_test.astype(np).reshape(-1, 1))
print(x_train_scaled)
# print(tf.__version__)
# print(sys.version_info)
# for module in mpl, np, pd, sklearn, tf, keras:
#     print(module.__name__, module.__version__)
model = keras.models.Sequential([
    # keras.layers.Flatten(input_shape=[28, 28]),
    keras.layers.Dense(300, activation='relu'),
    keras.layers.Dense(100, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# relu: y = max(0, x) softmax: 将向量变成概率分布x = [x1, x2, x3]
# y = [e^x1/sum, e^x2/sum, e^x3/sum], sum = e^x1 + e^x2 + e^x3
# reason for sparse: y->index. y->one_hot->[] 
model.compile(loss="sparse_categorical_crossentropy",
              optimizer = "sgd",
              metrics = ["accuracy"])    


logdir = './callbacks'
if not os.path.exists(logdir):
    os.mkdir(logdir)
output_model_file = os.path.join(logdir,
                                 "fashion_mnist_model.h5")

callbacks = [
    keras.callbacks.TensorBoard(logdir),
    keras.callbacks.ModelCheckpoint(output_model_file,
                                    save_best_only = True),
    keras.callbacks.EarlyStopping(patience=5, min_delta=1e-3),
]
history = model.fit(x_train_scaled, y_train, epochs=100,
                    validation_data=(x_valid_scaled, y_valid),
                    callbacks = callbacks)
# history = model.fit(x_train, y_train, epochs=10,
#                     validation_data=(x_valid, y_valid),
#                     callbacks = callbacks)                    
def plot_learning_curves(history):
    pd.DataFrame(history.history).plot(figsize=(8, 5))
    plt.grid(True)
    plt.gca().set_ylim(0, 1)
    plt.show()

plot_learning_curves(history)

# model.evaluate(x_test_scaled, y_test)
model.evaluate(x_test, y_test)
x
