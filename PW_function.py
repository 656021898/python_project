# -*-coding:utf-8-*-
import requests

host='test.admin.sosho.cn'
class PW_function:


    def login(account,password,area_code=86):
        login_data={'account':account,'password':password,'area_code':area_code}
        login_header={'appkey':'pwsite'}
        aa=print(requests.post('http://test.admin.sosho.cn/server/api/account/login',data=login_data,headers=login_header).json())
        #后面把这里改成拼接url，host+地址
        return aa
    #使用print(PW_function.login('18544444401','111111'))结果会多一个None，因为用print输出值，这个函数默认还有一个返回值为None

# PW_function.login('18544444401','111111')