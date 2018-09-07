# -*-coding:utf-8-*-

import pymysql
import time

#连接数据库
connect=pymysql.connect(host="test.sosho.cn",port=9696,user="ushoapi",password="usho85121608",db="usho2_test"
    #charset=''
)

i=0
while i<3:
    a = connect.cursor()
    #获取数据库游标对象
    update1 = "UPDATE usho_security_code SET is_invalid=0 WHERE mobile ='13355781026';"
    #将语句赋值在变量中
    print(a.execute(update1))
    time.sleep(10)
    #执行语句并返回结果
    i +=1
print('执行了%d次'%i)