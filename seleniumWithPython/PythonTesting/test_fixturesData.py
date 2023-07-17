import pytest

from PythonTesting.BaseClass import BaseClass


# ***You can have data setup seperately in a fixture in conftest.py file through which go to baseclass


@pytest.mark.usefixtures("dataLoad")
class TestExample(BaseClass): #going to baseclass

    def test_editProfile(self,dataLoad):
        log = self.getLogger()
        log.info(dataLoad)
        print(dataLoad)
        print(dataLoad[0])


