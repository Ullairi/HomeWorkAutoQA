import pytest
from simple_math import SimpleMath

@pytest.fixture
def simple_math():
    """Create a simple math instance"""
    return SimpleMath()

def test_square_pos(simple_math):
    assert simple_math.square(2) == 4
    assert simple_math.square(5) == 25

def test_square_neg(simple_math):
    assert simple_math.square(-3) == 9

def test_cube_pos(simple_math):
    assert simple_math.cube(3) == 27
    assert simple_math.cube(1) == 1

def test_cube_neg(simple_math):
    assert simple_math.cube(-3) == -27

def test_cube_null(simple_math):
    assert simple_math.cube(0) == 0