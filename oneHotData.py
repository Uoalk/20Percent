import csv

out=[]#clear vars

with open('cleanData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')#open file
    for row in csv_reader:#open file
        outLine=''  
        for item in row[:10]:#onehot data!
            if item == '1':#if rock
               outLine = outLine + "1,0,0," 
            elif item == '2':#if paper
               outLine = outLine + "0,1,0," 
            elif item == '3':#if scissors
               outLine = outLine + "0,0,1," 
            elif item == '0':#if n/a
               outLine = outLine + "0,0,0," 
            else:
                print("Error")#why would there be a number thats not 0-3
        out.append([outLine+str(row[10])+','+str(row[11])+','+str(row[12])])#save it to array

f= open("oneHot.csv","w")#save to new file
for row in out:
    f.write(str(row).replace("[","").replace("]","").replace("'","").replace(" ","")+"\n")
