def evaluate(n):
    if 1 <= n <= 100:
        if n % 2 == 0:
            if 2 <= n <= 5:
                return "Not Weird"
            else:
                if n > 20:
                    return "Not Weird"
                return "Weird"
        else:
            return "Weird"
    raise ValueError("Parameter n should be within [1; 100] range")


def calculate_3ops(arg1, arg2):
    def check_range(n):
        if 1 <= n <= 10000000000:
            return True
        raise ValueError("Parameter n should be within [1; 10,000,000,000] range")
    check_range(arg1)
    check_range(arg2)
    return [arg1 + arg2, arg1 - arg2, arg1 * arg2]


def divisions(a, b):
    return [a // b, a / b]


def generate_squares(limit):
    if 1 <= limit <= 20:
        for i in range(0, limit):
            yield i * i
    else:
        raise ValueError("Value must be within [1; 20] range")


def is_leap(some_year):
    leap = False
    if 1900 <= some_year <= 100000:
        if some_year % 400 == 0:
            leap = True
        elif some_year % 100 == 0:
            leap = False
        elif some_year % 4 == 0:
            leap = True
        return leap
    raise ValueError("Year must be within range [1900; 100,000]")


def cuboid_vectorization(maxx, maxy, maxz, exclusion):
    res = [
        [i, j, k]
        for i in range(0, maxx + 1)
        for j in range(0, maxy + 1)
        for k in range(0, maxz + 1)
        if i + j + k != exclusion]
    return res


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
