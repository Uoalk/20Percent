import csv

out=[]

with open('cleanData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        outLine=''
        for item in row[:10]:
            if item == '1':
               outLine = outLine + "1,0,0," 
            elif item == '2':
               outLine = outLine + "0,1,0," 
            elif item == '3':
               outLine = outLine + "0,0,1," 
            elif item == '0':
               outLine = outLine + "0,0,0," 
            else:
                print("Error")
        out.append([outLine+str(row[10])+','+str(row[11])+','+str(row[12])])

f= open("oneHot.csv","w")
for row in out:
    f.write(str(row).replace("[","").replace("]","").replace("'","").replace(" ","")+"\n")
