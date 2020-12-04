# -*-coding:utf-8-*-

import pytest
import requests


class Test_Case02:

    def setup(self):
        print ("-------->setup method!")
    
    def teardown(self):
        print ("++++++++teardown method!")
    
    def test_baidu(self):
        r = requests.get("http://www.baidu.com")
        assert r.status_code == 200
        assert  "baidu.com" in r.content

if __name__ == "__main__":
    pytest.main(['-s','-v','testcases/test_demo02.py','--alluredir','allure-results'])