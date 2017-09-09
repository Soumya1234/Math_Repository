from Matrix import *

"""
r0=[Complex(1,0),Complex(3,0),Complex(2,0)]
r1=[Complex(4,0),Complex(1,0),Complex(3,0)]
r2=[Complex(2,0),Complex(5,0),Complex(2,0)]
m=Matrix(3,3,Complex(0,0))
for i in range(m.row):
    for j in range(m.column):
        m.addValue(i,j,("r"+str(i))[j])
m.print_matrix()
"""
m=Matrix(3,3,Complex(0,0))
m.addValue (0,0,Complex(1,0))
m.addValue (0,1,Complex(3,0))
m.addValue (0,2,Complex(2,0))
m.addValue (1,0,Complex(4,0))
m.addValue (1,1,Complex(1,0))
m.addValue (1,2,Complex(3,0))
m.addValue (2,0,Complex(2,0))
m.addValue (2,1,Complex(5,0))
m.addValue (2,2,Complex(2,0))
m.print_matrix()
print m.det()
