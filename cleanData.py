#import
import csv

games = []
with open('uncleanedData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')#load dirty data
    line_count = 0
    i = 0#clear vars
    for row in csv_reader:
        if(row[2]=='0' or row[3]=='0'):#if one player timed out dont add data  
            pass
        else:#if both players played add the data
            games.append(row)

i=1
outData=[]#clear vars
while(i<len(games)):
    prevMoves=[0]*10
    n=1
    while(i-n>=1 and n<5 and games[i-n][0]==games[i][0]):#append any previous games the same players played
        prevMoves[(n-1)*2]=games[i-n][2]
        prevMoves[(n-1)*2+1]=games[i-n][3]
        n+=1

    #what should the computer have played?
    if(games[i][2]=="1"):
        perfectOut=["0","1","0"]
    if(games[i][2]=="2"):
        perfectOut=["0","0","1"]
    if(games[i][2]=="3"):
        perfectOut=["1","0","0"]
    outData.append([prevMoves+perfectOut])
    i+=1


f= open("cleanData.csv","w")#save the data
for row in outData:
    f.write(str(row).replace("[","").replace("]","").replace("'","").replace(" ","")+"\n")
