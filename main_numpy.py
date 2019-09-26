import numpy as np

if __name__ == '__main__':
    print(np.__version__)

    v = np.array([1, 2, 3])
    print(v)

    v[0] = 666
    print(v)
    v[0] = 1

    print(np.zeros(5))
    print(np.ones(5))
    print(np.full(5, 666))

    print('size =', v.size)
    print('size =', len(v))
    print(v[0:2])
    print(v[-1])

    v2 = np.array([4, 5, 6])
    print('{} + {} = {}'.format(v, v2, v + v2))
    print('{} - {} = {}'.format(v, v2, v - v2))
    print('{} * {} = {}'.format(v, v2, v * v2))
    print('Dot product of {} and {} = {}'.format(v, v2, np.dot(v, v2)))

    print(np.linalg.norm(v))
    print(v / np.linalg.norm(v))

    print(np.linalg.norm(v / np.linalg.norm(v)))

    # 逆矩阵
    v3 = np.array([[1, 2], [3, 4]])
    print('Inverse Matrix of \n {} is \n {}'.format(v3, np.linalg.inv(v3)))
    print('{}.dont({}) = {}'.format(v3, np.linalg.inv(v3), v3.dot(np.linalg.inv(v3))))
