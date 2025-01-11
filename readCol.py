import csv
with open('csv1.csv','r') as csv1:
    reader=csv.reader(csv1)
    header=next(reader)
    readerlist=list(reader)
    for i in range(0,len(header)):
        print(header[i])
        for row in readerlist:
            print(row[i])
        