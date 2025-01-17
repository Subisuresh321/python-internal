n=int(input("Enter the number: "))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

def factorial(x):
    if x==1 or x==0:
        return 1
    else:
        return x*factorial(x-1)
print(factorial(6))