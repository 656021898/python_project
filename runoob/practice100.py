# -*_ coding:utf-8 _*-
# 第1题是:有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#解法1
# list=[1,2,3,4]
# num = []
# for i in list :
#     for j in list:
#         for k in list:
#             if i != j != k :
#                 num.append(i*100+j*10+k)
#             # else:
#             #     continue
# print('共%d个，分别为%s'%(len(num),num))
#解法2（升级）
# list_num=[1,2,3,4]
# list = [
# i*100+j*10+k for i in list_num for j in list_num for k in list_num if(i!=j!=k)
# ]
# print(list)
#解法3
# import pprint #pprint库用来格式化输出
# list_num=['1','2','3','4']
# list_result=[]
# n=0
# for i in list_num:
#     for j in list_num:
#         for k in list_num:
#             if i!=j!=k :
#                 set = (i+j+k)
#                 print(set)
#                 n += 1
# print("能组成%d个互不相同且无重复数字的三位数: "%n)



# 第3题是:一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# list1=[]
# for i in range(40):
#     list1.append(i**2)
# for j in range(500):
#     if (j+100) in list1:
#         if (j+268) in list1:
#             print(j)
# 解法2：
# print([n**2-100 for m in range(168) for n in range(m) if(m+n)*(m-n)==168])
# for m in range(168):
#     for n in range(m,168):
#         if (n-m)*(n+m) == 168:
#             print(m**2-100)



# 第4题是:输入某年某月某日，判断这一天是这一年的第几天？
# year=int(input('请输入年份'))
# month=int(input('请输入月份'))
# day=int(input('请输入日子'))
# if (year % 4 ==0 and year % 100 != 0) or (year % 400 ==0):
#     if month <= 2:
#         print('共%d天' % ((month // 2) * 31 + ((month - 1) // 2) * 30 + day))
#     else:
#         print('共%d天' % ((month//2) * 31 + ((month - 1) // 2) * 30 - 1 + day))
# else:
#     if month<=2:
#         print('共%d天' % ((month // 2) * 31 + ((month - 1) // 2) * 30 + day))
#     else:
#         print('共%d天' % ((month // 2) * 31 + ((month - 1) // 2) * 30 - 2 + day))
#高手：
# year=int(input('请输入年份'))
# month=int(input('请输入月份'))
# day=int(input('请输入日子'))
# days=[31,28,31,30,31,60,31,30,31,30,31,30]
# if (year % 4 ==0 and year % 100 != 0) or (year % 400 ==0):
#     days[1] +=1
# print('共%d天'%(sum(days[0:(month-1)])+day))



#格式化处理日期
# import time
#
# data = input('请输入日期：')
# aa = time.strptime(data,'%Y-%m-%d')
# print(type(aa))
# a,b,c=aa[0:3]
# print(a,b,c)



# 第5题是:输入三个整数x,y,z，请把这三个数由小到大输出。
# x,y,z = input("请输入3个数").split()
# list1=[]
# list1.append(x,y,z)
# print(list1)





# 第6题是:斐波那契数列。
# 第7题是:将一个列表的数据复制到另一个列表中。
# 第8题是:输出 9*9 乘法口诀表。
# 第9题是:暂停一秒输出。
# 第10题是:暂停一秒输出，并格式化当前时间。
# 第11题是:古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 第12题是:判断101-200之间有多少个素数，并输出所有素数。
# 第13题是:打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。
# 第14题是:将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
# 第15题是:利用条件运算符的嵌套来完成此题：学习成绩&gt;=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
# 第16题是:输出指定格式的日期。
# 第17题是:输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# 第18题是:求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
# 第19题是:一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程找出1000以内的所有完数。
# 第20题是:一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
# 第21题是:猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
# 第23题是:打印出如下图案（菱形）:     *   ***  ***** *******  *****   ***    *
# 第24题是:有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
# 第25题是:求1+2!+3!+...+20!的和。
# 第26题是:利用递归方法求5!。
# 第27题是:利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
# 第28题是:有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
# 第29题是:给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
# 第30题是:一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
# 第31题是:请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# 第32题是:按相反的顺序输出列表的值。
# 第33题是:按逗号分隔列表。
# 第34题是:练习函数调用。
# 第35题是:文本颜色设置。
# 第36题是:求100之内的素数。
# 第37题是:对10个数进行排序。
# 第38题是:求一个3*3矩阵主对角线元素之和。
# 第39题是:有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
# 第40题是:将一个数组逆序输出。
# 第41题是:模仿静态变量的用法。
# 第42题是:学习使用auto定义变量的用法。
# 第43题是:模仿静态变量(static)另一案例。
# 第45题是:统计 1 到 100 之和。
# 第46题是:求输入数字的平方，如果平方运算后小于 50 则退出。
# 第47题是:两个变量值互换。
# 第48题是:数字比较。
# 第49题是:使用lambda来创建匿名函数。
# 第50题是:输出一个随机数。
# 第51题是:学习使用按位与 &amp; 。
# 第52题是:学习使用按位或 | 。
# 第53题是:学习使用按位异或 ^ 。
# 第54题是:取一个整数a从右端开始的4〜7位。
# 第55题是:学习使用按位取反~。
# 第56题是:画图，学用circle画圆形。
# 第57题是:画图，学用line画直线。
# 第58题是:画图，学用rectangle画方形。
# 第59题是:画图，综合例子。
# 第60题是:计算字符串长度。
# 第61题是:打印出杨辉三角形（要求打印出10行如下图）。
# 第62题是:查找字符串。
# 第63题是:画椭圆。
# 第64题是:利用ellipse 和 rectangle 画图。。
# 第65题是:一个最优美的图案。
# 第66题是:输入3个数a,b,c，按大小顺序输出。
# 第67题是:输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
# 第68题是:有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
# 第69题是:有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
n = int(input("请输入人数"))
# list1 = list(range(1,n+1))
# print(list1)
# list1.pop(n)
# print(list1)
while n >2 :
    list1 = list(range(1,n+1))
    print(list1)
    for i in range(1,n+1):
        if i % 3 == 0:
            list1.pop(i-1)
    n=len(list1)
print(n)


# 第70题是:写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。
# 第71题是:编写input()和output()函数输入，输出5个学生的数据记录。
# 第72题是:创建一个链表。
# 第73题是:反向输出一个链表。
# 第74题是:列表排序及连接。
# 第75题是:放松一下，算一道简单的题目。
# 第76题是:编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
# 第77题是:循环输出列表
# 第78题是:找到年龄最大的人，并输出。请找出程序中有什么问题。
# 第79题是:字符串排序。
# 第80题是:海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？
# 第81题是:809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。
# for i in range(10,100):
#     if (809*i==800*i+9*i) and (809*i<=9999) and (8*i<=99):
#         print(i,(809*i),(800*i+9*i))

# 第82题是:八进制转换为十进制
# 第83题是:求0—7所能组成的奇数个数。
# 第84题是:连接字符串。
# 第85题是:输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
# 第86题是:两个字符串连接程序。
# 第87题是:回答结果（结构体变量传递）。
# 第88题是:读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
# 第89题是:某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
# 第90题是:列表使用实例。
# 第91题是:时间函数举例1。
# 第92题是:时间函数举例2。
# 第93题是:时间函数举例3。
# 第94题是:时间函数举例4,一个猜数游戏，判断一个人反应快慢。
# 第95题是:字符串日期转换为易读的日期格式。
# 第96题是:计算字符串中子串出现的次数。
# 第97题是:从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
# 第98题是:从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件“test”中保存。
# 第99题是:有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
# 第100题是:列表转换为字典。