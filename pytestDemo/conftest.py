
# this is like a config. properties file in java
import pytest

# Initialisation (Before & after class):


@pytest.fixture(scope="class")
def setup():
    print("Launch Browser first")
    yield
    print("i will close browser")

# Multiple data (data-driven):


@pytest.fixture()
def dataTable():
    print("Creation of user credentials data")
    return ["olatundeoladeni@yahoo.com", "Ola", "123456", ]

# Multiple browser with multiple data (data-driven):


@pytest.fixture(params=[("chrome", "olatundeoladeni@yahoo.com", "Ola", "123456"), ("Firefox", "olatund.oladeni@yahoo.co.uk", "Ade", "Manchester"), ("IE", "olatundeoladeni@gmail.com", "Bola", "Lagos")])
def crossBrowser(request):
    return request.param

