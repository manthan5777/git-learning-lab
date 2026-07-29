import pytest

from app import add, subtract, multiply, divide, modulus, cube


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(4, 5) == 20


def test_divide():
    assert divide(20, 4) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_modulus():
    assert modulus(10, 3) == 1


def test_modulus_by_zero():
    with pytest.raises(ValueError):
        modulus(10, 0)


def test_cube():
    assert cube(3) == 27
