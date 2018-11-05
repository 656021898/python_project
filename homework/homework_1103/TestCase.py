import unittest
from homework.homework_1103.HttpRequest import HttpRequest

class TestCaseSetup(unittest.TestCase):
    def setUp(self):
        login_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
        login_data = {"mobilephone": "18688773467", "pwd": "123456"}
        login_res = HttpRequest(login_url, login_data, "post").httprequest()
        return login_res

    def test_case(self,url,data,method,code):
        res = HttpRequest(url=url,data=data,method=method).httprequest()
        try:
            self.assertEqual(code,res.json()["code"])
        except AssertionError as e:
            print("报错信息是：{}".format(e))

# login_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
# login_data = {"mobilephone": "18688773467", "pwd": "123456"}
# cookie = HttpRequest(login_url, login_data, "post").httprequest().cookies
# class TestCaseGlobal(unittest.TestCase):
#     def test_case(self):
#         recharge_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/recharge"
#         recharge_data = {"mobilephone": "18688773467", "amount": "123456"}
#         recharge_res = HttpRequest(recharge_url, recharge_data, "post").httprequest(cookie=cookie)
#         try:
#             self.assertEqual("登录成功",recharge_res.json()["msg"])
#         except AssertionError as e:
#             print("报错信息是：{}".format(e))


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run()


