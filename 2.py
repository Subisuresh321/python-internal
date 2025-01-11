class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
        
    def getArea(self):
        return self.l*self.b
    def getPeri(self):
        return 2*(self.l+self.b)
    def compare(self,other):
        if(self.getArea()>other.getArea()):
            print(f"{self.getArea()} is greater")
        else:
            print(f"{other.getArea()} is greater")
r1=Rectangle(2,4)
r2=Rectangle(3,4)
print(r1.getArea())
print(r2.getPeri())
r1.compare(r2)