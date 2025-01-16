import csv
with open('csv1.csv','r') as csv1:
    reader=csv.reader(csv1)
    header=next(reader)
    readerlist=list(reader)
    dict1={}
    for row in readerlist:
        dict1[row[0]]=len(row[0])
    print(dict1)
    dict2=dict(sorted(dict1.items(),key=lambda x: x[1]))
    print(dict2)
    
    dict_list=[{'Name':row[0],'Length':len(row[0])} for row in readerlist]
    print(dict_list)    
    

with open('csv2.csv','a+') as csv2:
    writer=csv.DictWriter(csv2,fieldnames=['Name','Length'])
    writer.writeheader()
    writer.writerows(dict_list)
        
    
        