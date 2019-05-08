#The file that takes in puzzle.csv to train the network and saves it as sudoku.h5.
#imports
from __future__ import absolute_import, division, print_function

import pathlib

import pandas as pd
import seaborn as sns

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.python.saved_model import tag_constants


#load training csvs
train_dataset = pd.read_csv('puzzle.csv')
train_label = pd.read_csv('answer.csv')

#define the model / neural network
def build_model():
  model = keras.Sequential([
    #5 layers 81 nodes > 500 > 1000 > 500 > 81
    layers.Dense(81, activation=tf.nn.relu, input_shape=[len(train_dataset.keys())]),
    layers.Dense(500, activation=tf.nn.relu),
    layers.Dense(1000, activation=tf.nn.relu),
    layers.Dense(500, activation=tf.nn.relu),
    layers.Dense(81)
  ])

  optimizer = tf.keras.optimizers.RMSprop(0.001)

  model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])#how will it change weights
  return model

class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')
    tf.keras.models.save_model(model, 'sudoku.h5')# save this every 100 runs or ~ 10 mins

model = build_model()#build the model

EPOCHS = 1000#how many times will it run

#this stops the training if it does not improve 10 times in a row
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

#start the training
history = model.fit(train_dataset, train_label, epochs=EPOCHS, validation_split = 0.2, verbose=0, callbacks=[early_stop, PrintDot()])

#save the model
tf.keras.models.save_model(model, 'sudoku.h5')