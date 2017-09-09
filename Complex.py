# This class provides the functionality of Complex Numbers
# Author: Soumyadeep Ganguly
import math
class Complex(object):
    #Constructor for the Complex object
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    #Overloaded "+" operator
    def __add__(self,complex_object):       
        return Complex(self.real+complex_object.real,self.imag+complex_object.imag)

    #Overloaded "-" operator
    def __sub__(self,complex_object):      
        return Complex(self.real-complex_object.real,self.imag-complex_object.imag)

     # Overloaded "*" operator
    def __mul__(self,a):
        return Complex(self.real*a.real-self.imag*a.imag,self.imag*a.real+self.real*a.imag)

    # Overloaded "/" operator
    def __div__(self,a):
        temp=Complex(0,0)
        temp=self*a.getConjugate()
        temp.real=temp.real/(a.getMagnitude()*a.getMagnitude())
        temp.imag=temp.imag/(a.getMagnitude()*a.getMagnitude())
        return temp

    # Function to get Magnitude of the Complex Number
    def getMagnitude(self):
        return math.sqrt(self.real*self.real+self.imag*self.imag)

    # Function to get Amplitude in Degree
    def getAmplitude(self):
        return (math.atan(float(self.imag)/float(self.real))*(180/math.pi))

    # Function to Obtain Complex Conjugate of the Complex Number 
    def getConjugate(self):
        return Complex(self.real,-self.imag)

    # String representation of the Complex Number in the "x+jy" form 
    def __repr__(self):
        if self.imag<0:
            return "%0.4f-j%0.4f" %(self.real,-self.imag)
        else:
            return "%0.4f+j%0.4f" %(self.real,self.imag)

    # Function for setting the Real Part
    def setReal(self,value):
        self.real=value
    
    #Function for setting the Imaginary part
    def setImag(self,value):
        self.imag=value



