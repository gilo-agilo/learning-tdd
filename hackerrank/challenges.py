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
