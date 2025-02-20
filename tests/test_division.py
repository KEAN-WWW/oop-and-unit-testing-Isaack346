import pytest

from App.Addition import addition
from App.Divide import divide

def test_division():
   # creating variables to test
    a = 10
    b = 10
    # Calling function
    assert divide(a,b) == 1

def test_divide_zero_exception():
    with pytest.raises(ZeroDivisionError):
        a = 10
        b = 0
        divide(a,b)
        pass