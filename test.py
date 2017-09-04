from Matrix import *

C1 = Complex(0, 0)
M1 = Matrix(2, 2, C1)
C2 = Complex(3, 3)
M1.print_matrix()
M2 = Matrix(2, 2, C2)
M2.print_matrix()
M3 = M1*M2
M3.print_matrix()



