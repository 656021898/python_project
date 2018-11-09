import requests

class TestHttpRequest:
    def __init__(self,url,data,method,code,cookie=""):
        self.url = url
        self.data = data
        self.method = str(method).lower()
        self.code = code
        self.cookie = cookie

    def HttpRequest(self):
        if self.method == "post":
            res = requests.post(url=self.url,data=self.data,cookies=self.cookie)
        elif self.method == "get":
            res = requests.get(url=self.url, params=self.data, cookies=self.cookie)
        else:
            print("请输入正确的method")
        return res

# if __name__ == "__main__":
    # login_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
    # login_data = {"mobilephone":"18544444402","pwd":"123456"}
    # login_res = TestHttpRequest(login_url,login_data,"post",111).HttpRequest()
    # print(login_res.cookies)
    # recharge_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/recharge"
    # recharge_data = {"mobilephone": "1854444402", "amount": "100"}
    # recharge_res = TestHttpRequest(recharge_url, recharge_data, "post",1111,cookie=login_res.cookies).HttpRequest()
    # print(recharge_res.json())
    #<RequestsCookieJar[<Cookie JSESSIONID=0390AB9F95D5D5B4D1E36599A11AB249 for 119.23.241.154/futureloan>]>

