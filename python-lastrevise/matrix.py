class Matrix:
    def __init__(self,matrix):
        self.matrix=matrix
    
    def get_transpose(self):
        transpose=[]
        for i in range (0,len(self.matrix[0])):
            row=[]
            for j in range(0,len(self.matrix)):
                row.append(self.matrix[j][i])
            transpose.append(row)
        return transpose
    
    def isupper(self):
        if(len(self.matrix)!=len(self.matrix[0])):
            print("NOT POSSIBLE")
            return False
        else:
            for i in range(1,len(self.matrix)):
                for j in range(0,i):
                    if(self.matrix[i][j]!=0):
                        return False
            return True
     
    def islower(self):
        if(len(self.matrix)!=len(self.matrix[0])):
            print("NOT POSSIBLE")
            return False
        else:
            for i in range(0,len(self.matrix)):
                for j in range(len(self.matrix[0])-1,i,-1):
                    if(self.matrix[i][j]!=0):
                        return False
            return True   
        
    def isdiagonal(self):
        if(self.islower() and self.isupper()):
            return True
        else:
            return False
    def maximum(self):
        maxx=-1
        for row in self.matrix:
            maxitem=max(row)
            maxx=max(maxx,maxitem)
        return maxx
        
m1=Matrix([[1,2,3],[4,10,6],[7,8,9]])
m3=Matrix([[1,0,0],[4,5,0],[7,8,9]])
m2=Matrix([[1,2,3],[0,5,6],[0,0,9]])
m4=Matrix([[1,0,0],[0,5,0],[0,0,9]])
print(m1.get_transpose())
print(m2.isupper())
print(m2.islower())
print(m3.isupper())
print(m3.islower())
print(m4.isdiagonal())
print(m3.isdiagonal())
print(m1.maximum())
