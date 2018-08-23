# -*-coding:utf-8-*-

import requests
import json

# url1= 'http://test.h5.sosho.cn/server/api/forum/access/topic/create'
form_data={"data": '{"result": {"model": "Homepage", "action": "BuildClass", "parameters": {"id": -6}}}'}

{"data":'{'
                  ''
                  '}
    'category_id':37,
    'title':111111,
    'cid':2000,
    'content': '[{"type":"text","value":"2222222222222222"}]'
'}
header={
    'expire':'1565943930',
    'token': 'cf358413c00f7e121463e2aebf65f6c5',
    'uid':'577921'
}
# aaa = requests.post(url=url1,data=json.dumps(body),headers=header)
print(requests.post('http://test.h5.sosho.cn/server/api/forum/access/topic/create',json=json.dumps(body),headers=header))
# print(aaa.json())


print(requests.get('http://test.h5.sosho.cn/mutual/my.html?cid=2000').content)
print(requests.get('http://test.h5.sosho.cn/server/api/forum/topics?cid=2000&per_page=15&page=1&is_my=true',headers=header).json())