# This class provides the functionality of Complex Numbers
# Author: Soumyadeep Ganguly
import math
class Complex(object):
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def show(self):
        if self.imag<0:
            print "%s-i%s" %(self.real,-self.imag)
        elif self.imag==0:
            print self.real
        else:
           print "%s+i%s" %(self.real,self.imag)
    
    def __add__(self,complex_object):
        _sum=Complex(0,0)
        _sum.real=self.real+complex_object.real
        _sum.imag=self.imag+complex_object.imag       
        return _sum

    def __sub__(self,complex_object):
        difference=Complex(0,0)
        difference.real=self.real-complex_object.real
        difference.imag=self.imag-complex_object.imag       
        return difference

    def getMagnitude(self):
        return math.sqrt(self.real*self.real+self.imag*self.imag)

    def getAmplitude(self):
        return (math.atan(float(self.imag)/float(self.real))*(180/math.pi))

    def getConjugate(self):
        temp=Complex(0,0)
        temp.real=self.real
        temp.imag=-self.imag
        return temp

    def __mul__(self,a):
        temp=Complex(0,0)
        temp.real=(self.real*a.real-self.imag*a.imag)
        temp.imag=(self.imag*a.real+self.real*a.imag)
        return temp

    def __div__(self,a):
        temp=Complex(0,0)
        temp=self*a.getConjugate()
        temp.real=temp.real/a.getMagnitude()
        temp.imag=temp.imag/a.getMagnitude()
        return temp



