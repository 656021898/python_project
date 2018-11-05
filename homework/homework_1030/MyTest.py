import unittest
from homework.homework_1030.MyHttpRequest import MyHttpRequest

#1、写用例TestCase
#2、执行用例：a、TestSuite存储用例  b、TestLoader找用例，加载用例，存储到TestSuite
#3、对比实际结果，断言
#4、出具测试报告TextTestRunner

class MyTest(unittest.TestCase):
    """
    一个函数就是一个用例
    不能传参
    """
    def setUp(self):
        self.login_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
        self.login_data = {"mobilephone": "18688773467", "pwd": "123456"}
        self.recharge_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/recharge"
        login_res = MyHttpRequest().http_request(url=self.login_url, data=self.login_data, method='post')
        return login_res

    def test_login_normal(self):
        login_res = MyHttpRequest().http_request(url=self.login_url, data=self.login_data, method='post')
        self.assertEqual('登录成功',login_res.json()['msg'])

    def test_login_pwd_null(self):
        login_data = {"mobilephone": "18688773467", "pwd": ""}
        login_res = MyHttpRequest().http_request(url=self.login_url, data=login_data, method='post')
        self.assertEqual('密码不能为空',login_res.json()['msg'])

    def test_login_mobilephone_null(self):
        login_data = {"mobilephone": "", "pwd": "123456"}
        login_res = MyHttpRequest().http_request(url=self.login_url, data=login_data, method='post')
        self.assertEqual('手机号不能为空',login_res.json()['msg'])

    def test_login_pwd_error(self):
        login_data = {"mobilephone": "18688773467", "pwd": "1234567"}
        login_res = MyHttpRequest().http_request(url=self.login_url, data=login_data, method='post')
        try:
            self.assertEqual('用户名或密码错误',login_res.json()['msg'])
        except AssertionError as error:
            print("错误是：{0}".format(error))

    def test_recharge_normal(self):
        recharge_data = {"mobilephone": "18688773467", "amount": "100"}
        recharge_res = MyHttpRequest().http_request(self.recharge_url, recharge_data, "get", self.setUp().cookies)
        try:
            self.assertEqual('充值成功',recharge_res.json()['msg'])
        except AssertionError as error:
            print("错误是：{0}".format(error))

    def test_recharge_mobilephone_null(self):
        recharge_data = {"mobilephone": "", "amount": "100"}
        recharge_res = MyHttpRequest().http_request(self.recharge_url, recharge_data, "get", self.setUp().cookies)
        try:
            self.assertEqual('手机号不能为空',recharge_res.json()['msg'])
        except AssertionError as error:
            print("错误是：{0}".format(error))

    def test_recharge_amount_null(self):
        recharge_data = {"mobilephone": "18688773467", "amount": ""}
        recharge_res = MyHttpRequest().http_request(self.recharge_url, recharge_data, "get", self.setUp().cookies)
        try:
            self.assertEqual('请输入金额',recharge_res.json()['msg'])
        except AssertionError as error:
            print("错误是：{0}".format(error))

    def test_recharge_amount_error(self):
        recharge_data = {"mobilephone": "18688773467", "amount": "-1"}
        recharge_res = MyHttpRequest().http_request(self.recharge_url, recharge_data, "get", self.setUp().cookies)
        try:
            self.assertEqual('请输入范围在0到50万之间的正数金额',recharge_res.json()['msg'])
        except AssertionError as error:
            print("错误是：{0}".format(error))

if __name__ =="__main__":
    unittest.main()
    # dir(unittest)
    #用来执行所有用例，根据用例的ASCII编码顺序执行，只能执行test开头的用例
    #鼠标放在用例旁边则只执行某条用例，放在unittest.main()则执行所有用例