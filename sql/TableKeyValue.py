import pymysql
import requests

class TableKeyValue:
    """
    这个类用来获取数据库某个表的key
    """
    def __init__(self,host,port,user,password,table_name,db=''):
        """
        获取必要的参数
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.table_name = table_name

    def Connect(self):
        """
        获取数据库连接
            cursor()用来创建一个新的游标并执行查询。
            游标的设计是一种数据缓冲区的思想，用来存放SQL语句执行的结果。
            先有数据基础：游标是在先从数据表中检索出数据之后才能继续灵活操作的技术。
            类似于指针：游标类似于指向数据结构堆栈中的指针，用来pop出所指向的数据，并且只能每次取一个。
        """
        connect_info = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db)
        my_connect = connect_info.cursor()
        return my_connect

    def get_key(self):
        """
        获取表中的key，并返回key_list
        """
        sql = 'SELECT * FROM ' + str(self.table_name)
        my_connect = self.Connect()
        my_connect.execute(sql)
        key_sets = my_connect.description
        key_list = []
        for key_set in key_sets:
            key_list.append(key_set[0])
        return key_list


if __name__ == '__main__':
    TableKeyValue('test.sosho.cn',9696,'ushoapi','usho85121608','usho_feature','usho2_test').get_key()

