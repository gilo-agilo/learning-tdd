def divisions(a, b):
    return [a // b, a / b]


def test_division():
    a = 4
    b = 3
    assert [1, 4 / 3] == divisions(a, b)


def print_lines(arr):
    for item in arr:
        print(item)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print_lines(divisions(a, b))
