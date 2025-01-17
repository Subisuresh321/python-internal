import math
a,b,c=map(int,input("Enter the valuse:").split())
dis=(b*b)-(4*a*c)
if dis>0:
    root1=(-b+math.sqrt(dis))/(2*a)
    root2=(-b-math.sqrt(dis))/(2*a)
    print(f"Root1 is {root1} and Root2 is {root2}")
elif dis==0:
    root1=root2=(-b)/(2*a)
    print(f"Root1 is {root1} and Root2 is {root2}")
else:
    real=-b/(2*a)
    img=math.sqrt((-dis))/(2*a)
    print(f"Root1 is {complex(real,img)} and Root2 is {complex(real,-img)}")
    
    
