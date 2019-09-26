from la.Matrix import Matrix
from la.Vector import Vector
import matplotlib.pyplot as plt

if __name__ == '__main__':
    points = [[0, 0], [0, 5], [3, 5], [3, 4], [1, 4],
              [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]]

    x = [point[0] for point in points]
    y = [point[1] for point in points]

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.plot(x, y)
    # plt.show()

    m = Matrix(points)
    t = Matrix([[2, 0], [0, 1.5]])  # 缩放
    t2 = Matrix([[1, 0], [0, -1]])  # x 轴翻转
    t3 = Matrix([[-1, 0], [0, 1]])  # y 轴翻转
    t4 = Matrix([[-1, 0], [0, -1]]) # 原点翻转

    m2 = t4.dot(m.transpose())

    plt.plot([m2.col_vector(i)[0] for i in range(m2.col_count())],
             [m2.col_vector(i)[1] for i in range(m2.col_count())])
    plt.show()
