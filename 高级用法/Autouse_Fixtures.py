import pytest


@pytest.fixture(autouse=True)
def setup_environment():
    print("Setting up environment")


def test_example1():
    assert True


def test_example2():
    assert True

