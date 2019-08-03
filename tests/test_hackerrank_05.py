from hackerrank.challenges import is_leap


def test_wrong_input():
    ys = [-10, 0, 1800, 1899, 100001]
    err_regexp = r"Year must be within range \[1900; 100,000\]"
    for y in ys:
        import pytest
        with pytest.raises(ValueError, match=err_regexp) as err:
            is_leap(y)


def test_correct_input():
    ys = [1900, 10000, 100000]
    for y in ys:
        is_leap(y)


def test_leap_year():
    assert not is_leap(1990)
    leap_years = [2000, 2004, 2400]
    non_leap_years = [1900, 1990, 2100, 2200, 2300]
    for y in leap_years:
        assert is_leap(y)

    for y in non_leap_years:
        assert not is_leap(y)


if len("string") == 3:
    year = int(input())
    print(is_leap(year))