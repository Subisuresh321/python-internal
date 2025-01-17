num=int(input("Enter the number: "))
sums=sum(int(i)**len(str(num)) for i in str(num))
if(num==sums):
    print("ams")