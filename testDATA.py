import random

lines=open("oneHot.csv").read().split("\n")
answers=[]

f = open("test.csv","w")
tests=100000;
for i in range(0,tests):
    line=random.choice(lines)
    
    f.write(str(line)[0:-6]+"\n")
    answers.append(str(line)[-5:])
f.flush()
play_dataset = pd.read_csv('test.csv', names=['P1.1r', 'P1.1p', 'P1.1s', 'P2.1r', 'P2.1p', 'P2.1s', 'P1.2r', 'P1.2p', 'P1.2s', 'P2.2r', 'P2.2p', 'P2.2s', 'P1.3r', 'P1.3p', 'P1.3s', 'P2.3r', 'P2.3p', 'P2.3s', 'P1.4r', 'P1.4p', 'P1.4s', 'P2.4r', 'P2.4p', 'P2.4s', 'P1.5r', 'P1.5p', 'P1.5s', 'P2.5r', 'P2.5p', 'P2.5s'], na_values = '?', sep=',')
pred = model.predict(play_dataset)
i = 0

wins=0
loss = 0
for item in pred:
    if item[0] > item[1] and item[0] > item[2]:
        if answers[i] == '1,0,0':
            wins+=1;
        if answers[i] == '0,1,0':
            loss+=1;
    elif item[1] > item[0] and item[1] > item[2]:
        if answers[i] == '0,1,0':
            wins+=1;
        if answers[i] == '0,0,1':
            loss+=1;
    elif item[2] > item[0] and item[2] > item[1]:
        if answers[i] == '0,0,1':
            wins+=1;
        if answers[i] == '1,0,0':
            loss+=1;
    i += 1
print(wins/tests)
print(loss/tests)
print((tests-wins-loss)/tests)