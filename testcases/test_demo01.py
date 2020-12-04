#-*-coding:utf-8-*-

import pytest
#import allure

class Test_Case01:
    def setup(self):
        print ("---->setup method")
    
    
    def test_a(self):
        print ("---->hello")
        assert 1
        
    
    def test_b(self):
        print ("---->hehe")
        assert 2 != 1

    def teardown(self):
        print ("---->teardown method")

if __name__ == "__main__":
    pytest.main(['-s','-v','testcases/test_demo01.py','-q','--alluredir','allure-results'])