# -*- coding:utf-8 -*-

# 1：用函数实现字符串a到z排列，不能用排序的函数，用代码实现
# def my_sort(my_str):
#     my_list = list(my_str)
#     for i in range(len(my_list)):
#         for j in range(i + 1, len(my_list)):
#             if ord(my_list[i]) > ord(my_list[j]):
#                 my_list[i], my_list[j] = my_list[j], my_list[i]
#     return ''.join(my_list)
#
#
# str1='lkjhgfdsa'
# print(my_sort(str1))

# -----------------------------------------------------------

# 2：请编程实现字符串的转换:将"adsdsfdndsdsdfsfdsdASDSDEDSFE"字符串大写变小写，小写变大写,并且将字符串变为镜像字符串,例如: 'A'变为A', 'b'变为'y'
# 注意：镜像字符串的用意，请自行去拓展了解。
# 大变小
# def my_str_lowercase(my_str):
#     new_str = ''
#     for i in my_str:
#         if 65<= ord(i) <=90:
#             new_str = new_str + chr(ord(i)+32)
#         else:
#             new_str = new_str + i
#     return new_str
#
#
# str1='dASDSDEDSFE'
# print(my_str_lowercase(str1))

#小变大
# def my_str_Capital(my_str):
#     new_str = list(my_str)
#     for i in new_str:
#         if 97<=ord(i)<=122:
#             new_str[new_str.index(i)] = chr(ord(i)-32)
#     my_str = ''.join(new_str)
#     return my_str
#
#
# str_capital="adsdsfdndsdsdfsfdsdASDSDEDSFE"
# print(my_str_Capital(str_capital))

#镜像字符串
# def str_mirror(my_str):
#     list1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#     list2 = list1.reverse()
#     # list2=['Z','Y','X','W','V','U','T','S','R','Q','P','O','N','M','L','K','J','I','H','G','F','E','D','C','B','A']
#     list3=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     list4=['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
#     new_str = ''
#     for i in my_str:
#         if 65<=ord(i)<=90:
#             new_str = new_str + list2[list1.index(i)]
#         elif 97<= ord(i) <=122:
#             new_str = new_str + list4[list3.index(i)]
#     return new_str
# str1='abcd'
# print(str_mirror(str1))
list1 = [1, 6, 7, 4, 5, 4, 5, 4, 5, 5, 6, 7, 8, 5, 6, 7, 3, 4, 2, 2, 1, 4, 8, 9, 4, 5, 6]
list1.remove(6,6,6)
print(list1)

# -----------------------------------------------------------

# 3：搜索引擎中会对用户输入的数据进行处理，第一步就是词法分析，分离字符串中的数字、中文、拼音、符号。
# 比如这个字符串:我的名字是monica,今年18岁。
# 词法分析后得到的结果如下结果:
# 数字:18
# 中文:我的名字是  今年 岁
# 拼音: Monica
# 请编写程，实现该词法分析功能。

# -----------------------------------------------------------

# 4：根据要求实现对应的方法（此题为拓展，请自行考虑关键词去进行百度搜索，辅助解题~重点是拓展自己的知识面）
# a) //等长的两个列表合并到一个字典
# 要求：合并成{"A":1,"B":2,"C":3},请用一行代码实现
# keys = ["A","B","C"]
# values = ["1","2","3"]
# print(dict(zip(keys,values)))

# b)//合并两个列表并消除重复值
# list_1 = ["a","b","c","1","A","winning"]
# list_2 = ["a","python","string","1"]
# print(list(set(list_1+list_2)))
#
# c) //已知一个列表，根据字典中的x，由大到小排序这个列表
# 已知列表：a = [{"x":1,"y":2},{"x":2,"y":3},{"x":3,"y":4}]
a = [{"x":1,"y":2},{"x":2,"y":3},{"x":3,"y":4}]
# for i in range(len(a)):
#     for j in range(i,len(a)):
#         if a[i]["x"] > a[j]["x"]:
#             a[i],a[j]=a[j],a[i]

# -----------------------------------------------------------

# 5:：编写一个程序：判断是否为等腰三角形
# def my_sort(a, b, c):
#     if a > b:
#         a, b = b, a
#     if b > c:
#         b, c = c, b
#     return a, b, c
#
#
# while True:
#     a, b, c = input("请输入三边,输入exit离开").split()
#     my_sort(a,b,c)
#     if (a + b > c) and ((a > 0) and (b > 0) and (c > 0)) and ((a == b) or (a == c) or (c == b)):
#         print("等腰")
#     else:
#         print("不是等腰")
#     aa = input("是否要继续，如果要继续输入Y，退出输入N")
#     if aa == 'Y':
#         continue
#     elif aa == 'N':
#         break


# -----------------------------------------------------------

# 6：编写一个程序实现阶乘：1×2×3×4...×n（请自行补充数学知识，啥是阶乘）
# def my_Factorial(num):
#     multiplier = 1
#     for i in range(1,(num+1)):
#         multiplier *= i
#     return multiplier
#
# print(my_Factorial(3))








