a=int(input("Enter the number a: "))
b=int(input("Enter the number b: "))
while(b):
    a,b=b,a%b
print(a)