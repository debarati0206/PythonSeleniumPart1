import pytest

@pytest.mark.skip
def test_firstProg():
    msg = "Hello"
    assert msg == "Hi", "Test failed"


@pytest.mark.smoke
def test_secondCreditCard():
    a=4
    b=6
    assert a+2==b,"Test case failed"
