import csv


games=[];
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    i=0
    for row in csv_reader:
        if(row[2]=='0' or row[3]=='0'):
            pass
        else:
            games.append(row)
        #print(row)

i=1
outData=[];
while(i<len(games)):
    prevMoves=[0]*10
    n=1
    while(i-n>=1 and n<5 and games[i-n][0]==games[i][0]):
        prevMoves[(n-1)*2]=games[i-n][2]
        prevMoves[(n-1)*2+1]=games[i-n][3]
        n+=1

    outData.append([prevMoves,[games[i][2],games[i][3]]])
    i+=1


f= open("cleanData.csv","w")
for row in outData:
    string=""
    for i in row[0] :
        string+=str(i)+","
    for i in row[1]:
        string+=str(i)+","
    string=string[:-1]
    f.write(string+"\n")
