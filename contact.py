# -*- conding:utf-8 -*-
import requests
# import json
# import PW_function
# import MW_function
#
# login_response=json.loads(PW_function.PW_function.login('18544444401','111111'))
# print(login_response['data']['name'])

#用json.dumps()把字典转换为字符串，json.loads()把字符串转换成字典
#json.dump()把数据写入json中，json.load()把文件打开，并把字符串变为数据类型
com_id=6
forms_url = 'http://test.h5.sosho.cn/server/api/community/join?com_id=' +str(com_id)
print(forms_url)
