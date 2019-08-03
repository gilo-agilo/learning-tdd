def cuboid_vectorization(maxx, maxy, maxz, exclusion):
    res = [
        [i, j, k]
        for i in range(0, maxx + 1)
        for j in range(0, maxy + 1)
        for k in range(0, maxz + 1)
        if i + j + k != exclusion]
    return res


def test_cuboid():
    a = 1
    b = 1
    c = 1
    N = 2
    res = cuboid_vectorization(a, b, c, N)
    assert res == [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

    a = 1
    b = 1
    c = 1
    N = 3
    res = cuboid_vectorization(a, b, c, N)
    assert res == [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0]]

    a = 2
    b = 2
    c = 2
    N = 3
    res = cuboid_vectorization(a, b, c, N)
    assert res == [[0, 0, 0], [0, 0, 1], [0, 0, 2],
                   [0, 1, 0], [0, 1, 1], [0, 2, 0], [0, 2, 2],
                   [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2], [1, 2, 1], [1, 2, 2],
                   [2, 0, 0], [2, 0, 2], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(cuboid_vectorization(x, y, z, n))
