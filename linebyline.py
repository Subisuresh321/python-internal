with open("text1.txt",'r') as txt1:
    list1=[]
    str1=" "
    while str1:
        str1=txt1.readline()
        list1.append(str1)
    print(list1)   