# Any pytest file should always start with => test_
# pytest method names should start with test_ e.g def test_firstProgram():
# Any code should be wrapped in method only
# Running all pytest from command line: C:\Users\olatu\PycharmProjects1\PythonProject1\PyTest>py.test -v -s
#  -k stands for tag in pytest is return in cmd as
# -v stands for generating log in pytest
# -s stands for getting more info in pytest
import pytest


@pytest.mark.regression
def test_assertProgram():
    mssg = "-Hello guys! I am learning pytest framework"
    assert mssg == "-Hello guys! I am learning pytest framework"


@pytest.mark.smoke
def test_assertNotProgram():
    msg = "-Python Automation getting interesting!"
    assert msg == "Manual testing", "Test failed because strings not match"


def test_fixtureMethod(setup):
    print("Enter url")

# This has been move to conftest file:
#@pytest.fixture()
#def setup():
    #print("Launch Browser first")
   # yield
    #print("i will close browser")




