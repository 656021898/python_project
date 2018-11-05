# -*_ coding:utf-8 _*-
import pymysql
import requests
from sql.TableKeyValue import *


class CommunityFeature:
    def __init__(self,host,port,user,password,com_id,db=''):
        """
        获取必要的参数
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.com_id = int(com_id)

    def default_creat(self):
        """把默认开通的模块自动生成"""
        h5 = requests.get('http://test.h5.sosho.cn/community/detail.html?id=' + str(self.com_id))
        print(h5)

    def all_feature(self):
        """获取所有的feature
        从usho_feature获取所有feature和对应数据，返回列表
        """
        my_tablename = 'usho_feature'
        sql = 'SELECT * from ' + my_tablename + ' WHERE id< 1000 and is_deleted=0;'
        my_connect = TableKeyValue(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db,table_name=my_tablename).Connect()
        my_key = TableKeyValue(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db,table_name=my_tablename).get_key()
        my_connect.execute(sql)
        result = list(my_connect.fetchall())  # fetchall()用来获取所有的结果行，且为set
        #获取allFeatureList
        allFeatureList = []
        for i in range(len(result)):
            dict1 = {}
            for j in my_key:
                dict1[j] = result[i][my_key.index(j)]
            allFeatureList.append(dict1)
        # 获取所有featureIdList
        featureIdList = []
        for list1 in result:
            featureIdList.append(list1[0])
        return allFeatureList,featureIdList

    def lack_feature(self):
        """
        #获取usho_community_feature中已添加的数据
        """
        my_tablename = 'usho_community_feature'
        sql = 'SELECT * from ' + my_tablename + ' WHERE is_deleted=0 and com_id={com_id};'.format(com_id=self.com_id)
        my_connect = TableKeyValue(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db,
                                   table_name=my_tablename).Connect()
        my_connect.execute(sql)
        #获取已经添加的featureId
        result = list(my_connect.fetchall())
        havaFeatureIdList = []
        for list1 in result:
            havaFeatureIdList.append(list1[2])
        #获取需要添加的featureId
        allFeatureList, featureIdList = self.all_feature()
        lackFeatureIdList = [i for i in featureIdList if i not in havaFeatureIdList]
        return lackFeatureIdList


    def creat_feature(self):
        """#创建feature"""
        #SELECT id FROM usho_feature ORDER BY id DESC LIMIT 1
        pass
        # self.default_creat(self.com_id)
        # self.all_feature()
        # sql_seach = 'SELECT* from usho_community_feature WHERE com_id=' + str(self.com_id) + ' AND is_deleted=0;'
        # self.aa.execute(sql_seach)
        # community_result = list(self.aa.fetchall())
        # # 获取已经添加过的feature_id
        # community_feature_id = []
        # for i in range(0, len(community_result)):
        #     community_feature_id.append(community_result[i][2])
        # print(community_feature_id)
        # # 获取需要添加的feature_id
        # creat_feature_id = list(set(self.all_feature()[0]).difference(set(community_feature_id)))
        # # 获取community_feature的最大id
        # next_id = self.aa.execute('')
        # for i in creat_feature_id:
        #     sql_insert = ''
        # print(creat_feature_id)
        # print(self.aa.fetchall())

#
if __name__ == '__main__':
    a1=CommunityFeature(host='test.sosho.cn',port=9696,user='ushoapi',password='usho85121608',com_id=3001,db='usho2_test')
    a1.lack_feature()
    # li1=a1.lack_feature()
    # li2 = a1.all_feature()[1]
    # print(len(li1),len(li2))

# aa = TableKeyValue('test.sosho.cn',9696,'ushoapi','usho85121608','usho_feature','usho2_test').Connect()
# print(aa)
