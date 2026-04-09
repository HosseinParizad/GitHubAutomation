from app.math_utils import sum_numbers

def test_sum():
    assert sum_numbers(1, 2) == 3

def test_sum_negative():
    assert sum_numbers(-1, 1) == 0