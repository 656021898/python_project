# -*- coding:utf-8 -*-

import requests
import json

class MW:
    def join_community(self,name,mobile,email,com_id):
        join_community_data={'data':json.dumps({
            "forms":[
                {"id":1,"value":name},
                {"id":12,"value":mobile},
                {"id":7,"value":email},
                {"id":17,"value":"北京科技职业学院"},
                {"id":22,"value":"大专"},
                {"id":19,"value":"2000"},
                {"id":18,"value":"计算机"},
                {"id":40,"value":""},
                {"id":1895,"value":""},
                {"id":1109,"value":""},
                {"id":1608,"value":""}],
            "joined_events":"{}",
            "com_id":com_id})}
        join_community_header={

        }