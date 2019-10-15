import pytest

def adds1(x: int):
    return x + 1

def test_adds1():
    assert adds1(4) == 5