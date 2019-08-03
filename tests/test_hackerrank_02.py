def check_range(n):
    if 1 <= n <= 10000000000:
        return True
    raise ValueError("Parameter n should be within [1; 10,000,000,000] range")


def calculate_3ops(arg1, arg2):
    check_range(arg1)
    check_range(arg2)
    return [arg1 + arg2, arg1 - arg2, arg1 * arg2]


def test_input_arg():
    params = [
        [0, 1],
        [1, 0],
        [0, 0],
        [100, 10000000001],
        [10000000001, 100]
    ]
    err_regex = r"Parameter n should be within \[1; 10,000,000,000\] range"
    for pair in params:
        import pytest
        with pytest.raises(ValueError, match=err_regex) as err:
            calculate_3ops(pair[0], pair[1])


def test_lines():
    n = 11
    m = 17
    res = calculate_3ops(n, m)
    assert res == [28, -6, 187]

    n = 3
    m = 2
    res = calculate_3ops(n, m)
    assert res == [5, 1, 6]


def print_lines(lines):
    for line in lines:
        print(line)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print_lines(calculate_3ops(a, b))