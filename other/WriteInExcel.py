# _-*-coding:utf-8 -*-

#往Excel内写入数据
import xlwt

excelname = xlwt.
sheet = excelname.add_sheet('循环添加')
    r'E:\jmeter\apache-jmeter-4.0\bin\sosho_test\用户登录MW并加入社群\写入数据.xlsx'
#写入文件路径
i=1
while i<5 :
    name = 'name'+str(i)
    mobile = 18500000000+i
    email = str(mobile)+'@qq.com'
    excelname.write(name,mobile,email)
excelname.save()


