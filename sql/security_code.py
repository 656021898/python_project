# -*_ coding:utf-8 _*-
import pymysql

connectInfo = pymysql.connect(
    host='test.sosho.cn',
    port=9696,
    user='ushoapi',
    password='usho85121608',
    db='usho2_test'
)

cur = connectInfo.cursor()

def recover(mobile) :
    if mobile == '':
        sql = 'UPDATE usho_security_code SET is_invalid=0'
    else:
        sql = 'UPDATE usho_security_code SET is_invalid=0 WHERE mobile = ' + str(mobile)
    return cur.execute(sql)



print(recover('13355781026',''))


