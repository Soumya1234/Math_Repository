from Matrix import *

C1 = Complex(1, 0)
m1 = Matrix(3, 3, C1)
m1.print_matrix()
C2=Complex(4,5)
m1.addValue(1,1,C2)
m1.getCoFactor(1,1).getCoFactor(0,0).print_matrix()


