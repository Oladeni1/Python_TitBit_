# Any pytest file should always start with => test_
# pytest method names should start with test_ e.g def test_firstProgram():
# Any code should be wrapped in method only
# Running all pytest from command line: C:\Users\olatu\PycharmProjects1\PythonProject1\PyTest>py.test -v -s
#  -k stands for method tag in pytest is return in cmd as
# -v stands for generating log in pytest
# -s stands for getting more info in pytest
# -m (mark) is used for test tagging like => smoke, regression , e2e in cmd as - m smoke
#  @pytest.mark.skip is to skip particular test(s) in pytest
import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo1(self):
        print("I will execute step in fixtureDemo method1 ")

    def test_fixtureDemo2(self):
        print("I will execute step in fixtureDemo method2 ")

    def test_fixtureDemo3(self):
        print("I will execute step in fixtureDemo method3 ")

    def test_fixtureDemo4(self):
        print("I will execute step in fixtureDemo method4 ")


