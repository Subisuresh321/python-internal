for i in range (1,10):
    if(i<=5):
        print("*"*i)
    else:
        print("*"*(10-i))

for i in range (1,6):
    for j in range (1,i+1):
        print(i*j,end=" ")
    print()