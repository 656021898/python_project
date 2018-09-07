# _-*-coding:utf-8 -*-

#往Excel内写入数据
import xlwt
import xlrd

#读
# # excelname = xlwt.Workbook(encoding='utf-8')
# excelname = xlrd.open_workbook(r'E:\jmeter\apache-jmeter-4.0\bin\sosho_test\用户登录MW并加入社群\写入数据.xls')
# #xlrd用来读取excel，URL=https://xlrd.readthedocs.io/en/latest/api.html
# sheet = excelname.sheets()[0]
# #sheets()用来获取sheet列表
# print(sheet)


#写
excelname = xlwt.Workbook()
sheet = excelname.add_sheet('写入的数据')
i = 1
while i<5:
    mobile = 18500000000 + i
    if i % 2 == 1:
        sheet.write(i,0,('name'+str(i)))
        sheet.write(i,1,mobile)
        sheet.write(i,2,(str(mobile) + '@qq.com'))
    else:
        sheet.write(i,0,('name'+str(i-1)))
        sheet.write(i,1,mobile)
        sheet.write(i,2,(str(mobile-1) + '@qq.com'))
    i += 1
excelname.save('E:\\jmeter\\apache-jmeter-4.0\\bin\\sosho_test\\用户登录MW并加入社群\\写入数据1.xls')
print('结束')


