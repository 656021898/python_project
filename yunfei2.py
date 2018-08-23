# -*-coding:utf-8-*-
#导入json库
import json

def_rang_nums=[0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,5,5,5,4,6,6,6]
def_rang_freights=[0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,2,2,2,2,2,2,2]
each_beyond_nums=[0,0,3,3,0,0,3,3,0,0,3,3,0,0,3,3,3,3,2,3,2,3,0]
each_beyond_freights=[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0]
quantitys=[1,3,5,100,300,500]

#计算件数运费的函数
def postage_amounts(def_rang_num=0,def_rang_freight=0,each_beyond_num=0,each_beyond_freight=0,quantity=0):
    #每增加0件的运费
    if each_beyond_num == 0:
        postage_amount = def_rang_freight
    #运费结果为小数时需要加1元
    elif (((quantity - def_rang_num) * each_beyond_freight) % each_beyond_num)> 0:
        postage_amount = def_rang_freight + (quantity - def_rang_num) * each_beyond_freight % each_beyond_num +1
    #运费结果为整数时，输出结果
    else:
        postage_amount = def_rang_freight + (quantity - def_rang_num) * each_beyond_freight / each_beyond_num
    return postage_amount


i=0
aa=0
j=0
#从购买件数的list中循环计算不同模板的运费
for j in range(len(quantitys)):
    #循环模板
    while i<len(def_rang_freights):
        aa = postage_amounts(def_rang_nums[i],def_rang_freights[i],each_beyond_nums[i],each_beyond_freights[i],quantitys[j])
        print('%d  '%aa,end='')
        i += 1
    print('\n')
    i = 0
    j += 1
