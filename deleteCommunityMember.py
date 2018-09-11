# -*_ coding:utf-8 _*-

import PW_function
import json
import requests

def delete_contact(mobile,password,com_id):
    print('删除中。。。。。')
    #管理员登陆并获取token
    resault = json.loads(PW_function.PW_function.login(account=mobile,password=password))
    access_token = str(resault['data']['access_token'])
    expire_timestamp = str(resault['data']['expire_timestamp'])
    uid = str(resault['data']['id'])

    #生成form表单和header
    form_data = {'cid': com_id,'per_page': 15,'is_verified': 1, 'is_chairman':'', 'is_admin':''}
    header = { 'appkey':'pwsite','access-token':access_token,'expire-timestamp':expire_timestamp, 'uid':uid}

    #获取联系人id列表
    request_url='http://test.admin.sosho.cn/server/api/contacts_manage/contacts'
    contact_list = json.loads(requests.post(url=request_url,data=form_data,headers=header).text)
        #requests.post(url=request_url,data=form_data,headers=header返回的结果是requests.models.Response，先把他的格式转成text，再解析
    num = contact_list['data']['counts']['total_items']

    while num > 0:  #开始循环获取contact_id并删除数据
        contact_list = json.loads(requests.post(url=request_url, data=form_data, headers=header).text)#重新获取联系人列表
        request_lists = contact_list['data']['items']#获取第一页items
        #将contact_id全部写入列表中
        id_lists=[]
        for request_list in request_lists:
            id_lists.append(request_list['_id'])
        #调用删除接口并删除数据
        i=0
        while i<len(id_lists):
            delete_url='http://test.admin.sosho.cn/server/api/contacts_manage/contacts/delete'
            form = {'cid':com_id,'contacts_ids':id_lists[i]}
            requests.post(url=delete_url,data=form,headers=header)
            i += 1
        del request_lists[:]#清空第一页items
        num = contact_list['data']['counts']['total_items']#重置num继续循环

    print('删除了%d条'%(len(id_lists)))



#调用函数并删除数据
delete_contact('18544444401','111111',2038)

