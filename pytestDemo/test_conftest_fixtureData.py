# Any pytest file should always start with => test_
# pytest method names should start with test_ e.g def test_firstProgram():
# Any code should be wrapped in method only
# Running all pytest from command line: C:\Users\olatu\PycharmProjects1\PythonProject1\PyTest>py.test -v -s
#  -k stands for method tag in pytest is return in cmd as
# -v stands for generating log in pytest
# -s stands for getting more info in pytest
# -m (mark) is used for test tagging like => smoke, regression , e2e in cmd as - m smoke
#  @pytest.mark.skip is to skip particular test(s) in pytest

# This explains data driven from conftest file:

import pytest

from pytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataTable")
class TestDataExample(BaseClass):    # Inheritance =>> LoggerClass

    def test_userCredential(self, dataTable):
        log = self.getLogs()  # Calling getLogs from LoggerClass
        log.info(dataTable[0])
        log.info(dataTable[1])
        log.info(dataTable[2])

        print(dataTable[0])
        print(dataTable[1])
        print(dataTable[2])

# Note: There is an issue running this test_conftest_fixtureData.py from cmd

