# -*- coding:utf-8 -*-

import requests
import json
import PW_function

class MW:

    def MW_account_register(self,mobile,scode,name,password,area_code=86):
        #注册接口
        login_data={
            'mobile':mobile,
            'password':password,
            'scode':scode,
            'name':name,
            'area_code':area_code
        }
        register_data=requests.post(url='http://test.h5.sosho.cn/server/account/register',data=register_data).json()
        print(register_data)
        return register_data

    def MW_account_login(self,mobile,password,area_code=86):
        #密码登录接口
        login_data={
            'account':mobile,
            'password':password,
            'area_code':area_code
        }
        login=requests.post(url='http://test.h5.sosho.cn/server/account/login',data=login_data).json()
        print(login)
        return login

    def MW_login_or_register(self,mobile,scode,area_code=86):
        #验证码登录接口
        login_data={
            'account':mobile,
            'scode':scode,
            'area_code':area_code
        }
        login=requests.post(url='http://test.h5.sosho.cn/server/account/login_or_register',data=login_data).json()
        print(login)
        return login


    def MW_account_bind(self):
        #微信绑定接口
        pass

    def community_forms(com_id):
        forms_url = 'http://test.h5.sosho.cn/server/api/community/join?com_id=' + str(com_id)
        forms_reponse=requests.get(url=forms_url).json()
        print(forms_reponse)
        return forms_reponse

    # def join_community(self,name,mobile,email,com_id):
    #     join_community_data={'data':json.dumps({
    #         "forms":[
    #             {"id":1,"value":name},
    #             {"id":12,"value":mobile},
    #             {"id":7,"value":email},
    #             {"id":17,"value":"北京科技职业学院"},
    #             {"id":22,"value":"大专"},
    #             {"id":19,"value":"2000"},
    #             {"id":18,"value":"计算机"},
    #             {"id":40,"value":""},
    #             {"id":1895,"value":""},
    #             {"id":1109,"value":""},
    #             {"id":1608,"value":""}],
    #         "joined_events":"{}",
    #         "com_id":com_id})}
    #     login_response = json.loads(MW_function.MW.join_community(mobile, '111111'))
    #     join_community_header={
    #         'user_id':login_response['data']['name'],
    #         'expire_timestamp':
    #     }
    #
    #     login_response = json.loads(MW_function.MW.join_community(mobile, '111111'))
    #     print(login_response['data']['name'])



MW.community_forms(com_id=2000)