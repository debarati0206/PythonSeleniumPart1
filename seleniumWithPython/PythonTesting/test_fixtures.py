import pytest


# def test_executeFirst(setup):
#     print("2nd execution")
#
#
# def test_execute2(setup):
#     print("3rd execution")
#
#
# def test_execute3(setup):
#     print("4th execution")


@pytest.mark.usefixtures("setup")
class TestExample2:

    def test_FixtureDemo1(self):
        print("1")

    def test_Demo2(self):
        print("2")
