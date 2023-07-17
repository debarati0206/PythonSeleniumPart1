import pytest


@pytest.fixture()
def setup():
    print("1st execution")
    yield
    print("5th execution")


@pytest.fixture()
def dataLoad():
    print("user details")
    return ["debarati","saha","debarati.a.saha@gmail.com"]


@pytest.fixture(params=["chrome", "firefox","IE"])
def CrossBrowser(request):
    return request.param


@pytest.fixture(params=[("chrome","debarati"), ("firefox","saha"),("IE","Automation")])
def MultiBrowser(request):
    return request.param
