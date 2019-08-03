def find_runner_up_score(n, arr):
    def check_value(item):
        if not (-100 <= item <= 100):
            raise ValueError('Value outside of range [-100; 100]')

    if 2 <= n <= 10:
        if len(arr) != n:
            raise ValueError('Array must have exactly {} items'.format(n))

        max = -200
        prev_max = max
        for i in range(0, n):
            check_value(arr[i])
            if arr[i] > max:
                prev_max = max
                max = arr[i]
            elif prev_max < arr[i] < max:
                prev_max = arr[i]

        return prev_max
    else:
        raise ValueError('Value outside of range [2; 10]')


def test_n_and_a():
    import pytest
    wrong_ns = [-1, 0, 1, 11]
    wrong_as = [[-101, 0, 1], [0, 1, 101], [0, 0, 200]]
    for a_n in wrong_ns:
        with pytest.raises(ValueError, match=r'Value outside of range \[2; 10\]'):
            find_runner_up_score(a_n, [])

    for an_a in wrong_as:
        with pytest.raises(ValueError, match=r'Value outside of range \[-100; 100\]'):
            find_runner_up_score(3, an_a)

    with pytest.raises(ValueError, match=r'Array must have exactly 3 items'):
        find_runner_up_score(n=3, arr=[1, 2, 3, 4])


def test_runner_up():
    dim = 6
    arr = [-3, 100, -20, 98, 99, 19]
    assert find_runner_up_score(dim, arr) == 99

    dim = 5
    arr = [2, 3, 6, 6, 5]
    assert find_runner_up_score(dim, arr) == 5


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(find_runner_up_score(n, list(arr)))