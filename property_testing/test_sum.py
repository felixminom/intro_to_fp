import pytest
from sum import sum

def test_sum():
    assert sum(1,2) == 3

from fixed_sum import sum as fixed_sum

@pytest.mark.parametrize(
    'num1, num2, expected',
    [(3,5,8),(-2,-2,-4), (-1,5,4), (3,-5,-2), (0,5,5)])
def test_sum_parametized(num1, num2, expected):
    assert fixed_sum(num1, num2) == expected

from hypothesis import given, settings, Verbosity, example
import hypothesis.strategies as st

@given(st.integers(), st.integers())
def test_sum_hypothesis(num1, num2):
    assert sum(num1, num2) == num1 + num2

@settings(verbosity=Verbosity.verbose)
@given(st.integers(), st.integers())
def test_sum_verbose(num1, num2):
    assert sum(num1, num2) == num1 + num2

@settings(verbosity=Verbosity.verbose)
@given(st.integers(), st.integers())
@example(1, 2)
def test_sum_verbose_with_example(num1, num2):
    assert sum(num1, num2) == num1 + num2

# Testing identity
@given(st.integers())
def test_sum_identity(num1):
    assert sum(num1, 0) == num1

# Testing commutative
@given(st.integers(), st.integers())
def test_sum(num1, num2):
    assert sum(num1, num2) == num2 + num1

@given(st.integers(), st.integers())
def test_sum_less_than_25(num1,num2):
    assert sum(num1, num2) == num1 + num2
    #assert num1 <= 25
