# -*_ coding:utf-8 _*-

import requests
import re

#从菜鸟获取100道练习的题目
num = 1
while num <=100:
    url = 'http://www.runoob.com/python/python-exercise-example'+str(num)+'.html'
    aa=requests.get(url=url)
    aa.encoding='utf-8'
    bb = '题目：(.*?) 程序分析：'
    cc = re.compile(bb).search(aa.text)
    # print(cc)
    if cc is None:
        num += 1
        continue
    else:
        dd = cc.group(1)
        print('第%d题是:%s'%(num,dd))
        num +=1



