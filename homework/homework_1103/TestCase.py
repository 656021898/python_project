import unittest
from homework.homework_1103.HttpRequest import HttpRequest

class TestCaseSetup(unittest.TestCase):

    def __init__(self,methodname,url,data,method,code):
        super(TestCaseSetup,self).__init__(methodname)#父类里面的__init__需要传入methodname
        self.url = url
        self.data = data
        self.method = method
        self.code = code

    def setUp(self):
        login_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
        login_data = {"mobilephone": "18688773467", "pwd": "123456"}
        login_res = HttpRequest(login_url, login_data, "post").httprequest()
        return login_res

    def test_case(self):
        res = HttpRequest(url=self.url,data=self.data,method=self.method,cookies=self.setUp().cookies).httprequest()
        try:
            self.assertEqual(self.code,res.json()["code"])
        except AssertionError as e:
            print("报错:"+e)


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run()


