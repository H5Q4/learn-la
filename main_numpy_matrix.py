import numpy as np

if __name__ == '__main__':
    A = np.array([[1, 2], [3, 4]])
    print(A)

    # 矩阵的属性
    print('Shape of \n {} is {}'.format(A, A.shape))
    print('Transpose of \n {} is \n {}'.format(A, A.T))

    # 获取矩阵的元素
    print(A[1, 1])
    print('First row of \n {} is {}'.format(A, A[0]))
    print('Second column of \n {} is {}'.format(A, A[:, 1]))

    # 矩阵基本运算
    B = np.array([[5, 6], [7, 8]])
    print(A + B)
    print(A - B)
    print(A * B)
    print(A.dot(B))

    V = np.array([4, 3])
    print(A.dot(V))
