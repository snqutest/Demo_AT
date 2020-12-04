#-*-coding:utf-8-*-

from xlrd import open_workbook

wb = open_workbook('./config/api_test.xlsx')

#根据工作表的名称获取表的内容
ws = wb.sheet_by_name('test_sheet')

#获取所有工作表的名称 
print (wb.sheet_names())

#通过工作表的索引
print (wb.sheet_by_index(0))

#获取工作表名称，行数和列数
print (ws.name)
print (ws.nrows,ws.ncols)

#获取第1行的内容，以列表形式表示
row1 = ws.row_values(0)

#获取第1列的内容，以列表形式表示
col1 = ws.col_values(0)

#通过行数值的多少遍历表格中的值
for i in range(0,ws.nrows):
    print (ws.row_values(i))

#获取单元格的值
print (ws.cell(0,0).value)
print (ws.cell(1,1).value)



