# -*- conding:utf-8 -*-
import requests
import json
import PW_function
import MW_function

# login_response = json.loads(MW_function.MW.MW_account_login(mobile, '111111'))
# print(login_response['data']['name'])

#用json.dumps()把字典转换为字符串，json.loads()把字符串转换成字典
#json.dump()把数据写入json中，json.load()把文件打开，并把字符串变为数据类型

aa={}
forms_resault = MW_function.MW.community_forms(2000)

join_forms = forms_resault['data']['join_forms']
input_forms={}

for join_form in join_forms:
    input_forms['id']=join_form['id']
    input_forms['value']=0

print('--------------')
for input_form in input_forms:
    print(input_forms)