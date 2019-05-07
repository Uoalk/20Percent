import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.saved_model import tag_constants
model = keras.models.load_model('main.h5')
lastPlays = [0]*30
wtl = [0,0,0]
inp = ''
comp = ''
while inp != 'q':
    f = open("sess.csv","w")
    f.write(str(lastPlays)[1:-1])
    f.flush()
    inp = input('What do you play? (r, p, s) ')
    play_dataset = pd.read_csv('sess.csv', names=['P1.1r', 'P1.1p', 'P1.1s', 'P2.1r', 'P2.1p', 'P2.1s', 'P1.2r', 'P1.2p', 'P1.2s', 'P2.2r', 'P2.2p', 'P2.2s', 'P1.3r', 'P1.3p', 'P1.3s', 'P2.3r', 'P2.3p', 'P2.3s', 'P1.4r', 'P1.4p', 'P1.4s', 'P2.4r', 'P2.4p', 'P2.4s', 'P1.5r', 'P1.5p', 'P1.5s', 'P2.5r', 'P2.5p', 'P2.5s'], na_values = '?', sep=',')
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
    print("The computer plays: " + comp)
    if inp == comp:
        wtl[1] += 1
        print("You tie")
    elif inp == 'r':
        if comp == 'p':
            wtl[2] += 1
            print("You lose")
        else:
            wtl[0] += 1
            print("You win")
    elif inp == 'p':
        if comp == 's':
            wtl[2] += 1
            print("You lose")
        else:
            wtl[0] += 1
            print("You win")
    elif inp == 's':
        if comp == 'r':
            wtl[2] += 1
            print("You lose")
        else:
            wtl[0] += 1
            print("You win")
    print("Your win percentage: " + str(100.0*wtl[0]/(wtl[0]+wtl[1]+wtl[2])))
    print("Computers win percentage: " + str(100.0*wtl[2]/(wtl[0]+wtl[1]+wtl[2])))
    lastPlays = tempOut + lastPlays[:24]