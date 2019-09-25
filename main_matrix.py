from la.Matrix import Matrix


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

