#-*-coding:utf-8-*-

import pytest




class Test_ABC:

    @pytest.fixture()
    def before(self):
        print ("---------->before")
    
    def test_a(self,before):        # test_a方法传入了被fixture标识的函数，以变量的形式
        print ("---------->test_a")
        assert 1

if __name__ == "__main__":
    pytest.main(['-s','-v','./testcases/test_demo04.py','--alluredir','./allure-results'])