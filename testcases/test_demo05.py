#-*-coding:utf-8-*-

import pytest

# fixture标记的函数可以应用于测试类外部,作用域为function,发现before会优先于测试类运行,且每个方法或函数会执行一次
@pytest.fixture(scope='class',autouse=True)    
def before():
    print ("--------->before execute")

@pytest.mark.usefixtures("before")
class Test_AAA:

    def setup(self):
        print ("------>setup method")
    
    def test_A(self):
        print ("------>test-A")
        assert 1
    
    def test_B(self):
        print ("------>test-B")
    
    def teardown(self):
        print ("------>teardown method")

if __name__ == "__main__":
    pytest.main(['-s','-v','./testcases/test_demo05.py','--alluredir','./allure-results'])

