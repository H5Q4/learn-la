from .Vector import Vector


class Matrix:
    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]

    @classmethod
    def zeros(cls, i, j):
        return Matrix([[0] * j for _ in range(i)])

    def dot(self, other):
        if isinstance(other, Vector):
            assert self.col_count() == len(other), \
                'Error in Matrix-Vector multiplication.'
            return Vector([self.row_vector(i).dot(other) for i in range(self.row_count())])
        if isinstance(other, Matrix):
            assert self.col_count() == other.col_count(), \
                'Error in Matrix-Matrix multiplication.'
            return Matrix([[self.row_vector(i).dot(other.col_vector(j)) for j in range(other.col_count())]
                           for i in range(self.row_count())])

    def transpose(self):
        return Matrix([[e for e in self.col_vector(i)] for i in range(self.col_count())])

    def __getitem__(self, item):
        i, j = item
        return self._values[i][j]

    def __add__(self, other):
        assert self.shape() == other.shape(), \
            'Error in adding, Shapes of matrices must be same.'
        return Matrix([[a + b for a, b in zip(self.row_vector(i), other.row_vector(i))]
                       for i in range(self.row_count())])

    def __sub__(self, other):
        assert self.shape() == other.shape(), \
            'Error in subtracting, Shapes of matrices must be same.'
        return Matrix([[a - b for a, b in zip(self.row_vector(i), other.row_vector(i))]
                       for i in range(self.row_count())])

    def __mul__(self, k):
        return Matrix([[e * k for e in self.row_vector(i)]
                       for i in range(self.row_count())])

    def __rmul__(self, k):
        return self * k

    def row_vector(self, index):
        return Vector(self._values[index])

    def col_vector(self, index):
        return Vector([row[index] for row in self._values])

    def row_count(self):
        return self.shape()[0]

    def col_count(self):
        return self.shape()[1]

    __len__ = row_count

    def size(self):
        a, b = self.shape()
        return a * b

    def shape(self):
        return len(self._values), len(self._values[0])

    def __repr__(self) -> str:
        return 'Matrix({})'.format(self._values)

    __str__ = __repr__
