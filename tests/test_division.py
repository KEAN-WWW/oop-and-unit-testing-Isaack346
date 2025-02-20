"""This is a test script tp test flask application"""
import pytest

from App.Divide import divide

def test_division():
    """test division"""
    a = 10
    b = 10
    # Calling function
    assert divide(a,b) == 1

def test_divide_zero_exception():
    """Test zero exception"""
    with pytest.raises(ZeroDivisionError):
        a = 10
        b = 0
        divide(a,b)
