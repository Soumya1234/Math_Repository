## This module is written to provide full functionality related to matrix algebra
## Author: Soumyadeep Ganguly
## Added from visual studio code

from Complex import *

class Matrix(object):

    #Constructor for the Matrix class. Constructs a (x * y) Matrix. Initializes all positions with "init_value"
    def __init__(self,x,y,init_value): #Passes a reference of a Complex Object "init_value"
        self.row=x
        self.column=y
        self.matrix_list=[[Complex(init_value.real,init_value.imag) for i in range(y)] for j in range(x)]
        
        
    #Function for printing the matrix in terminal
    def print_matrix(self):
        print "\n"
        for i in range(self.row):
            print self.matrix_list[i]
    
    #Function for returning value from the (i,j)th value
    def getValue(self,i,j):
        return self.matrix_list[i][j]

    #Function for adding a value "value" to the (i,j)th position in the matrix
    def addValue(self,i,j,value):
        self.matrix_list[i][j].setReal(value.real)
        self.matrix_list[i][j].setImag(value.imag)

    #Function for addition of Matrices
    def __add__(self,a):
        if self.row==a.row and self.column==a.column:
            sum=Matrix(self.row,self.column,Complex(0,0))
            for i in range(self.row):
                for j in range(self.column):
                    sum.matrix_list[i][j]=self.matrix_list[i][j]+a.matrix_list[i][j]
            return sum       
        else:
            raise Wrong_Dimensions,"Matrix Dimensions Mismatch"

    #Function for Multiplication of Matrices
    def __mul__(self,a):
        if self.column == a.row:
            product=Matrix(self.row,a.column,Complex(0,0))
            for x in range(self.row):
                for y in range(a.column):
                    sum=Complex(0,0)
                    for i in range(self.column):
                        sum=sum+self.matrix_list[x][i]*a.matrix_list[i][y]
                    product.matrix_list[x][y]=sum
            return product
        else:
            raise Wrong_Dimensions,"Matrices not compatiple for multiplication"
    
    #Function to obtain division by scalar
    def divideByScalar(self,a):
        temp=Matrix(self.row,self.column,Complex(0,0))
        for i in range(self.row):
            for j in range(self.column):
                temp.matrix_list[i][j]=self.matrix_list[i][j]/a
        return temp

    #Function for Cofactor Matrix of (a,b)th element
    def getCoFactorMatrix(self,a,b):
        if self.row==self.column:
            temp=Matrix(self.row-1,self.column-1,Complex(0,0))
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

    #Function to find out Determinant of the matrix
    def det(self):
        if self.row <> self.column:
            raise Wrong_Dimensions,"Determinant can only be found against square matrix"
        if self.row==1 and self.column==1:
            return self.matrix_list[0][0]
        else:
            sum=Complex(0,0)
            for j in range(self.column):
                x=self.matrix_list[0][j]*(self.getCoFactorMatrix(0,j).det())*((-1)**(1+(j+1)))
                sum=sum+x
            return sum
        
    #Function to obtain the Transpose of Matrix
    def transpose(self):
        temp=Matrix(self.column,self.row,Complex(0,0))
        for i in range(self.row):
            for j in range(self.column):
                temp.matrix_list[j][i]=self.matrix_list[i][j]
        return temp
    
    #Function to determine the cofactor of the (i,j)th element of the matrix
    def getCoFactor(self,i,j):
        return (self.getCoFactorMatrix(i,j).det())*((-1)**(i+1+(j+1)))
    
    #Function to determine the Adjoint matrix 
    def getAdjointMatrix(self):
        temp=Matrix(self.row,self.column,Complex(0,0))
        for i in range(self.row):
            for j in range(self.column):
                temp.matrix_list[i][j]=self.getCoFactor(i,j)
        return temp.transpose()
    
    #Function to obtain inverse of Matrix
    def inverse(self):
        temp=Matrix(self.row,self.column,Complex(0,0))
        for i in range(self.row):
            for j in range(self.column):
                temp.matrix_list[i][j]=self.getAdjointMatrix().divideByScalar(self.det()).matrix_list[i][j]
        return temp

    #Functio to add values from list
    def addFromList(self,a):
        k=0
        i=0
        j=0
        while k <= self.row*self.column-1:
            self.addValue(i,j,a[k])
            j=j+1
            if j==self.column-1:
                k=k+1
                self.addValue(i,j,a[k])
                i=i+1
                j=0
            k=k+1



#Exception class specific to Matrix Dimensions
class Wrong_Dimensions(Exception):
    def __init__(self,argument):
        self.message=argument
        

        
