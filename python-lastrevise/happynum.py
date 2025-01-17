num=int(input("Enter the number: "))
seen=set()
while(num!=1 and num not in seen):
    seen.add(num)
    num=sum(int(i)**2 for i in str(num))
if(num==1):
    print("It is happy ")
else:
    print("it is not haapy")