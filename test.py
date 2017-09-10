from Matrix import Matrix,Wrong_Dimensions
from Complex import Complex

m_list = [Complex(1,0),Complex(2,0),Complex(3,0),Complex(4,0)]
m = Matrix(2,2,Complex(0,0))
m.addFromList(m_list)
m.print_matrix()
