import pytest

# ** You can run test with multiple datasets using params in fixture declaration**
#data driven and parameterization can be done with return statement in list format using request


def test_crossBrowser(CrossBrowser):
    print(CrossBrowser)


def test_multiBrowser(MultiBrowser):
    print(MultiBrowser[1])
