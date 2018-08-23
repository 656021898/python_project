#-*-coding:utf-8-*-
def_range_num=int(input('请输入首重件数：'))
def_range_freight=int(input('请输入首重金额：'))
each_beyond_num=int(input('请输入增加件数：'))
each_beyond_freight=int(input('请输入增加金额：'))
quantity=int(input('请输入购买件数：'))

postage_amount=0
def yunfei(def_range_num=0,def_range_freight=0,each_beyond_num=0,each_beyond_freight=0,quantity=0):
    #计算首重
    if ((quantity-def_range_num)*each_beyond_freight % each_beyond_num) != 0:
        postage_amount = def_range_freight + (quantity - def_range_num) * each_beyond_freight / each_beyond_num + 1
    else:
        postage_amount = def_range_freight + (quantity - def_range_num) * each_beyond_freight / each_beyond_num

    return postage_amount
print('运费是：%d'%(yunfei(def_range_num,def_range_freight,each_beyond_num,each_beyond_freight,quantity)))
