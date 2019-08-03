def calculate_squares(limit):
    return list(generate_squares(limit))


def generate_squares(limit):
    if 1 <= limit <= 20:
        for i in range(0, limit):
            yield i * i
    else:
        raise ValueError("Value must be within [1; 20] range")


def print_results(limit):
    for item in generate_squares(limit):
        print(item)


def test_limit():
    ns = [0, -1, 21, 100]
    err_regex = r"Value must be within \[1; 20\] range"
    import pytest
    for N in ns:
        with pytest.raises(ValueError, match=err_regex) as err:
            calculate_squares(N)

    ns = [1, 3, 20]
    for N in ns:
        calculate_squares(N)


def test_calculate_squares():
    N = 5
    res = [0, 1, 4, 9, 16]
    assert res == calculate_squares(N)


if __name__ == '__main__':
    n = int(input())
    print_results(n)
