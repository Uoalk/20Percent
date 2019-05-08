#The file to load the stored network (sudoku.h5) and test it against a known good board.
#imports
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.saved_model import tag_constants

#load the model
model = keras.models.load_model('sudoku.h5')#chanage if you dont want the backup
#load the testing data
data = pd.read_csv('testing.csv')
#predict the board
prediction = model.predict(data)#add data

#print the predication
i = 0
for x in prediction[1]:
    if i % 9 == 0:
        print('')
    print(str(int(round(x))) + " ", end = "")
    i += 1

#print the real board
print("\n- - - - - - - - -")
#print("2 3 7 4 1 5 6 9 8\n9 6 5 8 3 7 2 1 4\n8 4 1 9 2 6 3 7 5\n3 7 9 2 5 1 8 4 6\n4 2 8 3 6 9 7 5 1\n5 1 6 7 4 8 9 2 3\n1 5 2 6 7 3 4 8 9\n6 9 4 5 8 2 1 3 7\n7 8 3 1 9 4 5 6 2")
print("8 7 1 2 6 4 3 9 5\n9 2 3 7 5 8 4 6 1\n4 6 5 3 1 9 2 7 8\n7 1 6 4 3 5 8 2 9\n5 9 4 8 2 6 1 3 7\n3 8 2 9 7 1 6 5 4\n6 5 7 1 4 2 9 8 3\n2 4 8 5 9 3 7 1 6\n1 3 9 6 8 7 5 4 2")
#print(prediction[0])#might not be [0]
