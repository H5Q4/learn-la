import math


class Vector:
    def __init__(self, lst):
        self._values = lst

    @classmethod
    def zero(cls, dim):
        return cls([0] * dim)

    def norm(self):
        return math.sqrt(sum(e ** 2 for e in self))

    def normalize(self):
        if math.isclose(self.norm(), 0):
            raise ZeroDivisionError('Normalize error! Norm is zero.')
        return self / self.norm()

    def dot(self, other):
        assert len(self) == len(other), \
            'Error in dot product. Length of vectors must be same'
        return sum(a * b for a, b in zip(self, other))

    def __add__(self, another):
        assert len(self) == len(another), \
            'Error in adding. Length of vectors must be same'
        return Vector([a + b for a, b in zip(self, another)])

    def __sub__(self, another):
        assert len(self) == len(another), \
            'Error in subtracting. Length of vectors must be same.'
        return Vector([a - b for a, b in zip(self, another)])

    def __mul__(self, k):
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        return self * k

    def __truediv__(self, other):
        return 1 / other * self

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    def __iter__(self):
        return self._values.__iter__()

    def __getitem__(self, index):
        return self._values[index]

    def __len__(self):
        return len(self._values)

    def __repr__(self):
        return 'Vector({})'.format(', '.join(str(e) for e in self._values))

    def __str__(self):
        return 'Vector({})'.format(', '.join(str(e) for e in self._values))
