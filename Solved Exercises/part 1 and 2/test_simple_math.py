import simple_math
import pytest

@pytest.mark.parametrize("n, m, expected", [
    (1, 2, 3),
    (6, 8, 14),
    (9, 6, 15)
])
def test_simple_add(n, m, expected):
    assert simple_math.simple_add(n, m) == expected

@pytest.mark.parametrize("n, m, expected", [
    (1, 2, -1),
    (6, 8, -2),
    (9, 6, 3)
])
def test_simple_sub(n, m, expected):
    assert simple_math.simple_sub(n, m) == expected


@pytest.mark.parametrize("n, m, expected", [
    (1, 2, 2),
    (6, 0, 0),
    (9, 6, 54)
])
def test_simple_mult(n, m, expected):
    assert simple_math.simple_mult(n, m) == expected

@pytest.mark.parametrize("n, m, expected", [
    (1, 0, float("inf")),
    (6, 3, 2),
    (1, 2, 0.5)
])
def test_simple_div(n, m, expected):
    assert simple_math.simple_div(n, m) == expected

def test_poly_first():
    assert simple_math.poly_first(2, 1, 3) == 7

def test_poly_second():
    assert simple_math.poly_second(2, 1, 3, 4) == 23
