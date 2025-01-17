dict1={'a':1,'e':2,'c':8,'b':4}
dict2=dict(sorted(dict1.items(),key=lambda item:item[1]))
dict3=dict(sorted(dict1.items()))
print(dict1,dict2,dict3)