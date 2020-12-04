#-*-coding:utf-8-*-
import pytest

@pytest.mark.smoke
class Test_yuema:

    def setup(self):
        print ("--->setup method")

    def test_a(self):
        print ('testing')    
        assert 1==1

    #fixture可以当做参数传入,用例调用fixture的返回值，直接就是把fixture的函数名称当做变量名称
    @pytest.fixture()
    def test_b(self):
        b = 'hehe'
        return b
      
    def test_c(self,test_b):
        assert test_b == 'hehe1'

    def teardown(self):
        print ("----->teardown method")

if __name__ == "__main__":
    pytest.main(['-s','-v','./testcases/test_demo03.py','--alluredir','./allure-results'])