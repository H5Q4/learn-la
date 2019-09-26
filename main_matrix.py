from la.Matrix import Matrix
from la.Vector import Vector


if __name__ == '__main__':
    m = Matrix([[1, 2, 3], [4, 5, 6]])

    print(m)
    print('Shape of {} is {}'.format(m, m.shape()))
    print('size of {} is {}'.format(m, m.size()))
    print('row {} in {} is {}'.format(1, m, m.row_vector(1)))
    print('column {} in {} is {}'.format(1, m, m.col_vector(1)))

    m2 = Matrix([[3, 2, 1], [6, 5, 4]])
    print('{} + {} = {}'.format(m, m2, m + m2))
    print('{} - {} = {}'.format(m, m2, m - m2))
    print('{} * {} = {}'.format(m, 2, m * 2))
    print('{} * {} = {}'.format(2, m, 2 * m))

    print('Zero_2_3 = {}'.format(Matrix.zeros(2, 3)))

    m3 = Matrix([[1, 2], [3, 4]])
    m4 = Matrix([[5, 6], [7, 8]])
    v = Vector([3, 2])
    print('Matrix-Vector:', m3.dot(v))
    print('m3.dot(m4):', m3.dot(m4))
    print('m4.dot(m3):', m4.dot(m3))

    print('Transpose of {} is {}'.format(m3, m3.transpose()))

    i = Matrix.identity(2)
    print('I =', i)
    print('m3.dot(I) =', m3.dot(i))

