# -*- coding:utf-8 -*-
#一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
# 编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，然后显示一条消息指出这个人是否可以加入球队
# 询问10次后，输出满足条件的总人数。
num = 1
people = 0
while num <= 10:
    try:
        sex,age = input('请输入性别（m表示男性，f表示女性）、年龄,用空格隔开:').split()
        if sex == 'f' and 10 <= int(age) <= 12:
            people += 1
        num += 1
    except ValueError:
        print('数据不合规，请重新输入')
print('已经询问了10个人，符合条件的有{0}人'.format(people))

# 输入num为四位数，对其按照如下的规则进行加密：
# 1）每一位分别加5，然后分别将其替换为该数除以10取余后的结果
# 2）将该数的第1位和第4为互换，第二位和第三位互换
# 3）最后合起来作为加密后的整数输出
num = input('请输入一个四位数')
list1 = []
for i in range(len(num)):
    list1.append(int(num[i])+5)
    list1[i] = list1[i] % 7
j=0
k=-1
while j < (len(list1)/2):
    m = list1[j]
    list1[j] = str(list1[k])
    list1[k] = str(m)
    j += 1
    k += -1
num=''.join(list1) # 把list中的字符串串起来
print(int(num))

# 一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣
# 如果购买金额大于100元会给20%折扣。
# 编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格
price = float(input('请输入价格'))
if price<50 :
    print('价格为{0}'.format('%.2f'%price))
elif 50<= price <=100 :
    print('价格为{0}'.format('%.2f' % (price*0.9)))
else:
    print('价格为{0}'.format('%.2f' % (price * 0.8)))

# 生成随机整数，从1-9取出来。
# 然后输入一个数字，来猜，如果大于，则打印bigger。
# 小了，则打印less。如果相等，则打印equal
import random
num = random.randint(1,9)
num2 = int(input('请输入一个数字:'))
if num2>num :
    print('bigger')
elif num2 < num :
    print('less')
else:
    print('equal')
