# 要求如下：
# 1）针对10-27号写的http_request类做作业
#
# 2）提供2个接口：登录url='http://119.23.241.154:8080/futureloan/mvc/api/member/login'~~mobilephone:18688773467~~pwd:123456
# 充值：'http://119.23.241.154:8080/futureloan/mvc/api/member/recharge' 参数请参考老师的Python文件mobilephont:18688773467~~amount:100
# 3）针对登录接口写4个用例  ：正常登录、  不输入密码 、 不输入账号一个、 输入错误的密码
# 充值接口写4个用例：正常充值、  不输入账号、不输入金额一个 、输入错误的金额负数
# 4）请利用任何一种方法实现用例的加载并执行
# 5）生成html类型的测试报告
# 注意：请在测试类里面加上异常处理以及断言
import requests

class MyHttpRequest:

    def http_request(self,url,data,method='',cookie=None):
        if method.lower() == 'get':
            res = requests.get(url,data,cookies=cookie)
        else:
            res = requests.post(url,data,cookies=cookie)
        return res


if __name__ == "__main__":
    # 登陆
    login_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
    login_data = {"mobilephone": "18688773467", "pwd": "123456"}
    login_res = MyHttpRequest().http_request(url=login_url, data=login_data, method='post')
    print(login_res.json())

    # 充值
    recharge_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/recharge"
    recharge_data = {"mobilephone": "18688773467", "amount": "-1"}
    recharge_res = MyHttpRequest().http_request(recharge_url, recharge_data, "get", login_res.cookies)
    print(recharge_res.json())