## This module is written to provide full functionality related to matrix algebra
## Author: Soumyadeep Ganguly
## Added from visual studio code

from Complex import *

class Matrix(object):

    #Constructor for the Matrix class. Constructs a (x * y) Matrix. Initializes all positions with "init_value"
    def __init__(self,x,y,init_value): #Passes a reference of a Complex Object "init_value"
        self.row=x
        self.column=y
        self.matrix_list=[[Complex(init_value.getReal(),init_value.getImag()) for i in range(y)] for j in range(x)]

    #Function for printing the matrix in terminal
    def print_matrix(self):
        for i in range(self.row):
            print self.matrix_list[i]
    
    #Function for returning value from the (i,j)th value
    def getValue(self,i,j):
        return self.matrix_list[i][j]

    #Function for adding a value "value" to the (i,j)th position in the matrix
    def addValue(self,i,j,value):
        self.matrix_list[i][j].setReal(value.getReal())
        self.matrix_list[i][j].setImag(value.getImag())

    #Function for addition of Matrices
    def addToMatrix(self,a):
        if self.row==a.row and self.column==a.column:
            sum=Matrix(self.row,self.column,None)
            for i in range(self.row):
                for j in range(self.column):
                    sum.matrix_list[i][j]=self.matrix_list[i][j]+a.matrix_list[i][j]
            return sum       
        else:
            raise Wrong_Dimensions,"Matrix Dimensions Mismatch"

    #Function for Multiplication of Matrices
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

    #Function for Cofactor of (a,b)th element
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

#Exception class specific to Matrix Dimensions
class Wrong_Dimensions(Exception):
    def __init__(self,argument):
        self.message=argument
        

        
