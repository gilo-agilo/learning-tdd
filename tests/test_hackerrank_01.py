import math
import os
import random
import re
import sys
import pytest


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


def test_input():
    err_msg_regex = r"Parameter n should be within \[1; 100\] range"
    with pytest.raises(ValueError, match=err_msg_regex) as err:
        evaluate(0)

    evaluate(100)

    with pytest.raises(ValueError, match=err_msg_regex) as err:
        evaluate(120)


def test_odd_n():
    k = 1
    n = 2*k + 1
    res = evaluate(n)
    assert "Weird" == res


def test_even_and_in_range25():
    k = 2
    n = 2*k
    assert 2 <= n <= 5

    res = evaluate(n)
    assert "Not Weird" == res


def test_even_and_in_range620():
    k = 5
    n = 2*k
    assert 6 <= n <= 20

    res = evaluate(n)
    assert "Weird" == res


def test_even_and_gt20():
    k = 11
    n = 2*k
    assert n > 20

    res = evaluate(n)
    assert "Not Weird" == res


if __name__ == '__main__':
    n = int(input().strip())
    print(evaluate(n))
