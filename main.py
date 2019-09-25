from la.Vector import Vector

if __name__ == "__main__":
    v = Vector([5, 2])
    print(v)
    print('Length of {} is {}'.format(v, len(v)))
    print('v[0] = {}, v[1] = {}'.format(v[0], v[1]))
    v2 = Vector([3, 1])
    k = 2
    print('{} + {} = {}'.format(v, v2, v + v2))
    print('{} - {} = {}'.format(v, v2, v - v2))
    print('{} * {} = {}'.format(v, k, v * k))
    print('{} * {} = {}'.format(k, v, k * v))

    zero = Vector.zero(3)
    print('zero vector: {}'.format(zero))

    print('norm of {} = {}'.format(v, v.norm()))

    print('normalize({}) = {}'.format(v, v.normalize()))
    print('normalize({}).length = {}'.format(v, v.normalize().norm()))

    try:
        zero.normalize()
    except ZeroDivisionError:
        print('Cannot normalize zero vector {}'.format(zero))

    print('Dot product of {} and {} is {}'.format(v, v2, v.dot(v2)))

