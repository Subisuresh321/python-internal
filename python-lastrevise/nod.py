num=int(input("Enter the number: "))
count=0
while(num):
    num//=10
    count+=1
print(count)