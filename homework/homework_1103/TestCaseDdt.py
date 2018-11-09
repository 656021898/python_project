from ddt import ddt,data,file_data,unpack
import unittest

# @ddt
# class TestCaseSetupDdt(unittest.TestCase):
#
#     def setUp(self):
#         login_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
#         login_data = {"mobilephone": "18688773467", "pwd": "123456"}
#         login_res = HttpRequest(login_url, login_data, "post").httprequest()
#         return login_res
#
#     def test_case(self,url,data,method,code):
#         res = HttpRequest(url=self.url,data=self.data,method=self.method,cookies=self.setUp().cookies).httprequest()
#         try:
#             self.assertEqual(self.code,res.json()["code"])
#         except AssertionError as e:
#             print("报错:"+e)


def addnum():
    print("")


print(addnum().__class__)