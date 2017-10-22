from Matrix import Matrix,Wrong_Dimensions
from Complex import Complex

m_list = [Complex(1,0),Complex(2,0),Complex(3,0),Complex(4,0)]
m_list2 = [Complex(1,0),Complex(2,0),Complex(3,0),Complex(4,0)]
m1 = Matrix(2,2,Complex(0,0))
m2 = Matrix(2,2,Complex(0,0))
m1.addFromList(m_list)
m2.addFromList(m_list2)
(m1+m2).print_matrix()
m1.inverse().print_matrix()
m1.transpose().print_matrix()
m1.getAdjointMatrix().print_matrix()
print m1.det()
