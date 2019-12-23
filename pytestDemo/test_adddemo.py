# Any pytest file should always start with => test_
# pytest method names should start with test_ e.g def test_firstProgram():
# Any code should be wrapped in method only
# Running all pytest from command line: C:\Users\olatu\PycharmProjects1\PythonProject1\PyTest>py.test -v -s
#  -k stands for tag in pytest is return in cmd as
# -v stands for generating log in pytest
# -s stands for getting more info in pytest
import pytest


@pytest.mark.smoke
def test_addition():
    a = 100
    b = 200
    assert a + 50 == 150, "Sum is true"


@pytest.mark.regression
def test_Newaddition():
    a = 100
    b = 200
    assert a + b - 50 == 150, "Sum is not true"










