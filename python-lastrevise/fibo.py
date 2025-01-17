limit=int(input("Enter the number: "))
f1=0
f2=1
f3=0
for i in range(0,limit):
    f3=f1+f2
    print(f1)
    f1=f2
    f2=f3