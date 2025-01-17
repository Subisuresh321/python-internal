num=int(input("Enter the number: "))
numstring=str(num)
temp=num
sum=0
while(num):
    i=num%10
    sum+=pow(i,len(numstring))
    num//=10
if sum==temp:
    print("It is amstrong ")
else:
    print("it is not")
    