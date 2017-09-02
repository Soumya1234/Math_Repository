## This module is written to provide full functionality related to matrix algebra
## authored by Soumyadeep Ganguly
class Matrix(object):
    def __init__(self,x,y,init_value):
        self.row=x
        self.column=y
        self.matrix_list=[[init_value for i in range(y)] for j in range(x)]
    
    def print_matrix(self):
        for i in range(self.row):
            print self.matrix_list[i]
    
    def addValue(self,i,j,value):
        self.matrix_list[i][j]=value

    def addToMatrix(self,a):
        if self.row==a.row and self.column==a.column:
            sum=Matrix(self.row,self.column,None)
            for i in range(self.row):
                for j in range(self.column):
                    sum.matrix_list[i][j]=self.matrix_list[i][j]+a.matrix_list[i][j]
            return sum       
        else:
            raise Wrong_Dimensions,"Matrix Dimensions Mismatch"
    
    def multiplyTo(self,a):
        if self.column == a.row:
            product=Matrix(self.row,a.column,None)
            for x in range(self.row):
                for y in range(a.column):
                    sum=0
                    for i in range(self.column):
                        sum=sum+self.matrix_list[x][i]*a.matrix_list[i][y]
                    product.matrix_list[x][y]=sum
            return product
        else:
            raise Wrong_Dimensions,"Matrices not compatiple for multiplication"
        
    def getCoFactor(self,a,b):
        if self.row==self.column:
            temp=Matrix(self.row-1,self.column-1,None)
            i=0
            j=0
            for r in range(self.row):
                for c in range(self.column):
                    if(r != a and c != b):
                        temp.matrix_list[i][j]=self.matrix_list[r][c]
                        j=j+1
                        if(j==self.column-1):
                            j=0
                            i=i+1
            return temp
        else:
            raise Wrong_Dimensions,"Co factor can only be found against square matrix"
        
class Wrong_Dimensions(Exception):
    def __init__(self,argument):
        self.message=argument
        

        
