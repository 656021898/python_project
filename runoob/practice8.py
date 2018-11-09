# 1.比如自然数10以下能被3或者5整除的有,3,5,6和9，那么这些数字的和为23.
# 求能被3或者5整除的1000以内数字的和
# sum = 0
# for i in range(1, 1000):
#     if (i % 3 == 0) or (i % 5 == 0):
#         sum += i
# print(sum)

# 2.在一个数组指定数组里面移除指定的数字,并返回新的数组并从大到小排序
# 比如:
# nums=[1,6,6,3,6,2,10,2,100],remove_num=6
# 要求返回时nums=[1, 2, 3, 10, 100]
# def removenum(num,my_list=[]):
#     if num not in my_list:
#         print("{0}不在列表中".format(num))
#     while num in my_list:
#         my_list.remove(num)
#     my_list.sort()
#     print(my_list)
# nums=[1,6,6,3,6,2,10,2,100]
# remove_num=11
# removenum(remove_num,nums)
# 3.从排序好的任意数组列表里面删除重复元素(你不知道列表里面有多少个重逢的元素)
# 比如:
# nums=[1,3,3,5,5,8,10,10,100,100],处理完之后是:[1, 3, 5, 8, 10, 100]
# nums=[1,3,3,5,5,8,10,10,100,100]
# def removeRepest(nums=[]):
#     for i in nums:
#         while nums.count(i)>1:
#             nums.remove(i)
#     print(nums)
# nums=[1,3,3,3,3,3,3,3,5,3,5,8,8,8,5,8,10,10,100,100]
# removeRepest(nums)
# 4.从排好序的数组里面，删除重复的元素.重复的数字最多只能出现2次
# nums=[1,1,1,2,2,3]
# 要求返回nums=[1,1,2,2,3]
# def removeRepest(nums=[]):
#     for i in nums:
#         while nums.count(i)>2:
#             nums.remove(i)
#     print(nums)
# nums=[1,3,3,3,3,3,3,3,5,3,5,8,8,8,5,8,10,10,100,100]
# removeRepest(nums)
# 5.给定2个字符串s1,s2,判定s2能否给s1做循环移位得到字符串的包含。比如:
# s1="AABBCDAACD",s2="CDAA".
# def aaa(strlong,strshort):
#     sum = 0
#     if len(strshort)>len(strlong):
#         print("无法循环得到")
#     strdouble = strlong + strlong[0:len(strshort)-1]
#     for i in range(len(strdouble)-len(strshort)):
#         if strdouble[i:(i+len(strshort))] == strshort:
#             sum += 1
#             continue
#         else:
#             continue
#     if sum ==0:
#         print("无法循环得到")
#     else:
#         print("可以得到{aa}个".format(aa=sum))
#
# aaa("AABBCDAACD","CDAA")
# 6.给定一个字符串,寻找没有字符串重复的最长子字符串.
# 比如:"abcabcbb" 找到的是"abc",长度为3，比如"bbbbb"找到的是"b",长度为1
#获取所有子串
def Substring(strvalue):
    strlist =[]
    for i in range(0,len(strvalue)):
        # i为0，1，2，3。。。。len(srtvalue)-1，子串的长度为len(strvalue)-i
        for j in range(i+1):
            substring = strvalue[j:(len(strvalue)-i+j)]
            list1=[]
            for a in substring:
                list1.append(a)
            if len(list1) > len(list(set(list1))):
                continue
            else:
                strlist.append(substring)
    strlist = list(set(strlist))
    strlist.sort(key = lambda i:len(i),reverse=True)#根据字符串的长度，从大到小排序
    print(strlist,"hahahah")
    #从子串列表中打印最长的几个
    for k in range(len(strlist)):
        if k < len(strlist)-1:
            if len(strlist[k]) > len(strlist[k+1]):
                print(strlist[:k+1])
                break
        elif k==len(strlist)-1:
            print(strlist)
            break

Substring("dfgdfghgfd")
# print("888")
# Substring("bbbbb")
# print("888")
# # Substring("abcdefg")
print("******************************************************")
str1 = "dfgdfghgfd"
list2 = []

for i in range(len(str1)):
    list1 = []
    print(str1[i:])
    for a in str1[i:]:
        if str1.index(a) ==len(str1)-1:
            list2.append("".join(list1))
            break
        else:
            if a not in list1:
                list1.append(a)
            else:
                list2.append("".join(list1))
                break
    # list2.append("".join(list1))
print(list2)
list2 = list(set(list2))
list2.sort(key = lambda i:len(i),reverse=True)#根据字符串的长度，从大到小排序
print(list2,"hahahah")
#从子串列表中打印最长的几个
for k in range(len(list2)):
    if k < len(list2)-1:
        if len(list2[k]) > len(list2[k+1]):
            print(list2[:k+1])
            break
    elif k==len(list2)-1:
        print(list2)
        break






# 7.有一串长的字符串 names="LI XIA  ,ZHAO MING  ,LAO WANG *,DA XIONG >,LI MEI MEI," \
#       "CHANG JIANG,LI QIANG,ZHANG WU JI,ZHANG SAN FENG," \
#       "DU GU QIU BAI,QIAO FENG"
# 要求：
# 1).过滤出所以的名字，去掉每个名字的左右的空格和乱码，每个名字的首字母大小
# 比如'LAO WANG *'，处理成'Lao wang'
# 2).统计出所以名字里面名字最常的
# 3).统计出同姓的人名单
#
# names="LI XIA  ,ZHAO MING  ,LAO WANG *,DA XIONG >,LI MEI MEI," "CHANG JIANG,LI QIANG,ZHANG WU JI,ZHANG SAN FENG," "DU GU QIU BAI,QIAO FENG"
#
#
# 8.数字1到5可以被写成:one,two,three,four,five,因此这些字母的总长度为:
# 3+3+5+4+4=19,现在求序列1到1000(包括1000),这些数字写成单词，总长度为多少
# 比如 342(three hundred and forty-two)为23字母,空格和-不计算.
# 比如 115(one hundred and fifteen)为20个字母
# 比如 1000(one hundred)为11个字母
# def numforenglish():
#     num1_english = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"elven",
#                     12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen ",18:"eighteen ",19:"nineteen"}
#     num10_english = {20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninty"}
#     sum =0
#     for i in range(333,334):
#         num100=i // 100
#         num10 = (i % 100) // 10
#         num1 = (i%100)%10
#         # print(num100, num10, num1,num1_english[num100],num1_english[num10*10+num1], (len(num1_english[num100]) + len("hundred") + len("and") + len(num1_english[num10*10+num1])),end="  ")
#         if num100 != 0 :
#             if (num10 != 0) and (num10 != 1):
#                 if num1 != 0:
#                     english_num = len(num1_english[num100]) + len("hundred") + len("and")+len(num10_english[num10*10])+len(num1_english[num1])
#                 else:
#                     english_num = len(num1_english[num100]) + len("hundred") + len("and") + len(num10_english[num10 * 10])
#             elif num10 == 1:
#                 english_num = len(num1_english[num100]) + len("hundred") + len("and") + len(num1_english[num10*10+num1])
#             else:
#                 if num1 != 0:
#                     english_num = len(num1_english[num100]) + len("hundred") + len("and") + len(num1_english[num1])
#                 else:
#                     english_num = len(num1_english[num100]) + len("hundred")
#         else:
#             if (num10 != 0) and (num10 != 1):
#                 if num1 !=0:
#                     english_num = len(num10_english[num10*10])+len(num1_english[num1])
#                 else:
#                     english_num = len(num10_english[num10 * 10])
#             elif num10 == 1:
#                 english_num =len(num1_english[num10*10+num1])
#             else:
#                 if num1 != 0:
#                     english_num = len(num1_english[num100]) + len("hundred") + len("and") + len(num1_english[num1])
#                 else:
#                     english_num = len(num1_english[num100]) + len("hundred")
#         print(i,english_num)
#         sum += english_num
#         # print("")
#     print(sum)
#
# numforenglish()





