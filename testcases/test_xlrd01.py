#*-*-coding:utf-8-*-

from xlrd import open_workbook
import requests
import time
import pytest

class V2ex_test:
    def setup(self,path):
        self.path = path
        self.baseurl = 'https://www.v2ex.com/api/'
    
    
    def load_excel(self):
        #打开excel文件
        excel = open_workbook(self.path)
        table = excel.sheet_names()[0]
        #获取工作表格的行数
        nrows = table.nrows
        
        #循环遍历数据，将他存到list中去
        test_data = []
        for i in range(1,nrows):
            #print (table.row_values(i))
            test_data.append(table.row_values(i))
        return test_data
    
    def test_v2ex_site():
        requests.request(method=test_data,url= self.path + '')


    def teardown(self):
        pass


if __name__ == "__main__":
    pytest.main(['-s','-v','./testcases/test_xlrd01.py','--alluredir','./allure-results'])      

