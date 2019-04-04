from __future__ import absolute_import, division, print_function

import pathlib

import pandas as pd
import seaborn as sns

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.python.saved_model import tag_constants

column_names = ['P1.1r', 'P1.1p', 'P1.1s', 'P2.1r', 'P2.1p', 'P2.1s', 'P1.2r', 'P1.2p', 'P1.2s', 'P2.2r', 'P2.2p', 'P2.2s', 'P1.3r', 'P1.3p', 'P1.3s', 'P2.3r', 'P2.3p', 'P2.3s', 'P1.4r', 'P1.4p', 'P1.4s', 'P2.4r', 'P2.4p', 'P2.4s', 'P1.5r', 'P1.5p', 'P1.5s', 'P2.5r', 'P2.5p', 'P2.5s', 'R.r', 'R.p', 'R.s']
raw_dataset = pd.read_csv('oneHot.csv', names=column_names, na_values = "?", sep=",")

train_dataset = raw_dataset.copy()
train_label = raw_dataset.copy()

train_dataset.pop('R.r')
train_dataset.pop('R.p')
train_dataset.pop('R.s')

train_label.pop('P1.1r')
train_label.pop('P1.1p')
train_label.pop('P1.1s')
train_label.pop('P2.1r')
train_label.pop('P2.1p')
train_label.pop('P2.1s')

train_label.pop('P1.2r')
train_label.pop('P1.2p')
train_label.pop('P1.2s')
train_label.pop('P2.2r')
train_label.pop('P2.2p')
train_label.pop('P2.2s')

train_label.pop('P1.3r')
train_label.pop('P1.3p')
train_label.pop('P1.3s')
train_label.pop('P2.3r')
train_label.pop('P2.3p')
train_label.pop('P2.3s')

train_label.pop('P1.4r')
train_label.pop('P1.4p')
train_label.pop('P1.4s')
train_label.pop('P2.4r')
train_label.pop('P2.4p')
train_label.pop('P2.4s')

train_label.pop('P1.5r')
train_label.pop('P1.5p')
train_label.pop('P1.5s')
train_label.pop('P2.5r')
train_label.pop('P2.5p')
train_label.pop('P2.5s')

def build_model():
  print("yeet")
  model = keras.Sequential([
    layers.Dense(64, activation=tf.nn.relu, input_shape=[len(train_dataset.keys())]),
    layers.Dense(64, activation=tf.nn.relu),
    layers.Dense(3)
  ])

  optimizer = tf.keras.optimizers.RMSprop(0.001)

  model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])
  return model

class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')

model = build_model()

EPOCHS = 1000

early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

history = model.fit(train_dataset, train_label, epochs=EPOCHS, validation_split = 0.2, verbose=0, callbacks=[early_stop, PrintDot()])

lastPlays = [0]*30
wtl = [0,0,0]
inp = ''
comp = ''
while inp != 'q':
    f = open("test.csv","w")
    f.write(str(lastPlays)[1:-1])
    f.flush()
    inp = input('Play : ')
    play_dataset = pd.read_csv('test.csv', names=['P1.1r', 'P1.1p', 'P1.1s', 'P2.1r', 'P2.1p', 'P2.1s', 'P1.2r', 'P1.2p', 'P1.2s', 'P2.2r', 'P2.2p', 'P2.2s', 'P1.3r', 'P1.3p', 'P1.3s', 'P2.3r', 'P2.3p', 'P2.3s', 'P1.4r', 'P1.4p', 'P1.4s', 'P2.4r', 'P2.4p', 'P2.4s', 'P1.5r', 'P1.5p', 'P1.5s', 'P2.5r', 'P2.5p', 'P2.5s'], na_values = '?', sep=',')
    pred = model.predict(play_dataset)
    if pred[0][0] > pred[0][1] and pred[0][0] > pred[0][2]:
        comp = 'r'
    elif pred[0][1] > pred[0][0] and pred[0][1] > pred[0][2]:
        comp = 'p'
    elif pred[0][2] > pred[0][0] and pred[0][2] > pred[0][1]:
        comp = 's'
    tempOut = []
    if inp == 'r':
        tempOut = [1,0,0]
    elif inp == 'p':
        tempOut = [0,1,0]
    elif inp == 's':
        tempOut = [0,0,1]
    if comp == 'r':
        tempOut = tempOut + [1,0,0]
    elif comp == 'p':
        tempOut = tempOut +[0,1,0]
    elif comp == '2':
        tempOut = tempOut + [0,0,1]
    if inp == comp:
        wtl[1] += 1
    elif inp == 'r':
        if comp == 'p':
            wtl[2] += 1
        else:
            wtl[0] += 1
    elif inp == 'p':
        if comp == 's':
            wtl[2] += 1
        else:
            wtl[0] += 1
    elif inp == 's':
        if comp == 'r':
            wtl[2] += 1
        else:
            wtl[0] += 1
    print(comp)
    print(wtl)
    lastPlays = tempOut + lastPlays[:24]