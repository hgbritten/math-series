from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_one():
  actual = fibonacci(1)
  expected = 1
  assert actual == expected

def test_zero():
  actual = fibonacci(0)
  expected = 0
  assert actual == expected

def test_two():
  actual = fibonacci(2)
  expected = 1
  assert actual == expected

def test_three():
  actual = fibonacci(3)
  expected = 2
  assert actual == expected

def test_four():
  actual = fibonacci(4)
  expected = 3
  assert actual == expected

def test_five():
  actual = fibonacci(5)
  expected = 5
  assert actual == expected

def test_six():
  actual = fibonacci(6)
  expected = 8
  assert actual == expected

def test_zero_l():
  actual = lucas(0)
  expected = 2
  assert actual == expected

def test_one_l():
  actual = lucas(1)
  expected = 1
  assert actual == expected

def test_two_l():
  actual = lucas(2)
  expected = 3
  assert actual == expected

def test_three_l():
  actual = lucas(3)
  expected = 4
  assert actual == expected

def test_four_l():
  actual = lucas(4)
  expected = 7
  assert actual == expected

def test_five_l():
  actual = lucas(5)
  expected = 11
  assert actual == expected

def test_six_l():
  actual = lucas(6)
  expected = 18
  assert actual == expected

def test_zero_s():
  actual = sum_series(0)
  expected = 0
  assert actual == expected

def test_zero_sl():
  actual = sum_series(0,2,1)
  expected = 2
  assert actual == expected

def test_one_s():
  actual = sum_series(1)
  expected = 1
  assert actual == expected

def test_one_sl():
  actual = sum_series(1,2,1)
  expected = 1
  assert actual == expected

def test_two_sl():
  actual = sum_series(2,2,1)
  expected = 3
  assert actual == expected

def test_three_sl():
  actual = sum_series(3,2,1)
  expected = 4
  assert actual == expected

def test_four_sl():
  actual = sum_series(4,2,1)
  expected = 7
  assert actual == expected

def test_four_s():
  actual = fibonacci(4)
  expected = 3
  assert actual == expected

def test_five_s():
  actual = fibonacci(5)
  expected = 5
  assert actual == expected

def test_six_s():
  actual = fibonacci(6)
  expected = 8
  assert actual == expected