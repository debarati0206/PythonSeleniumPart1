# any pytest file will start with test_ or end with _test
#pytest method starts with test_
#any code should be wrapped in method always
import pytest




@pytest.mark.smoke
def test_firstProg():
    print("Hello")


def test_secondProg(setup):
    print("Bad morning!")


@pytest.mark.xfail
def test_thirdProg():
    print("this will execute but will not show the status ")
