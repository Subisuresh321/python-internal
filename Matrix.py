class Matrix:
    def __init__(self,data):
        self.data=data
    def gettranspose(self):
        traspose=[]
        for i in range (0,len(self.data[0])):
            tr_row=[]
            for row in self.data:
                tr_row.append(row[i])
            traspose.append(tr_row)
        print(traspose)
    
    def isupper(self):
        if(len(self.data)!=len(self.data[0])):
            return False
        for i in range(1,len(self.data)):
            for j in range(i):
                if(self.data[i][j]!=0):
                    return False
        return True
                    
    def islower(self):
            if(len(self.data)!=len(self.data[0])):
                return False
            for i in range(len(self.data)):
                for j in range(i+1,len(self.data)):
                    if(self.data[i][j]!=0):
                        return False
            return True
        
    def isdiagonal(self):
        if(self.isupper() and self.islower()):
            return True
        else:
            return False
        
    def getMinMax(self):
        min=max=self.data[0][0]
        for i in range (len(self.data)):
            for j in range(len(self.data[0])):
                if(min>self.data[i][j]):
                    min=self.data[i][j]
                if(max<self.data[i][j]):
                    max=self.data[i][j]
        return min,max
    
data1=[[1,2],[0,5]]
data2=[[1,0,0],[2,3,0],[7,8,9]]
data3=[[1,0,0],[0,3,0],[0,0,9]]
data4=[[7,8,3],[4,5,6],[7,8,9]]
m1=Matrix(data4)
m1.gettranspose()
print(m1.isupper())
print(m1.islower())
print(m1.isdiagonal())
a,b=m1.getMinMax()
print(f"The min is {a} and max is {b}")