# 1：写一个函数，可以完成任意指定整数的相加，并返回结果
def my_sum(*num):
    sum=0
    for i in num:
        sum += i
    return sum


print(my_sum(1,2,3,4,5,6))


# 2：自动贩卖机： 只接受1元、5元、10元的纸币或硬币，可以1块，5元，10元。最多不超过10块钱。
# 饮料只有橙汁、椰汁、矿泉水、早餐奶，售价分别是3.5，4，2，4.5
# 写一个函数用来表示贩卖机的功能： 用户投钱和选择饮料，并通过判断之后，给用户吐出饮料和找零。
def vending_machine():
    drinks = {"橙汁": 3.5, "椰汁": 4, "矿泉水": 2, "早餐奶": 4.5}
    money_sum = 0
    drink = input("请输入您要购买的饮料，橙汁、椰汁、矿泉水、早餐奶")
    if drink in drinks.keys():
        while money_sum < drinks[drink]:
            money = int(input("请投币"))
            if money in [1, 5, 10]:
                money_sum += money
            else:
                print("投入的金额只能为1元、5元、10元的纸币或硬币")
                continue
        if money_sum == drinks[drink]:
            print("这是您的饮料:{0}，欢迎下次光临".format(drink))
        else:
            print("这是您的饮料:{0}，这是您的找零{1}元".format(drink, (money_sum - drinks[drink])))
    else:
        print("您购买的饮料暂未上架")


vending_machine()


# 3、写函数，将姓名、性别，城市作为参数，并且性别默认为f(女)。
# 如果城市是在长沙并且性别为女，则输出姓名、性别、城市，并返回True,否则返回False。
def what(name, city, sex='f'):
    if city == '长沙' and sex == 'f':
        print('姓名是:{0}，性别是：{1}，城市是：{2}'.format(name, sex, city))
        return True
    else:
        print('姓名是:{0}，性别是：{1}，城市是：{2}'.format(name, sex, city))
        return False


name, city, sex = input("请输入姓名、城市、性别，用逗号隔开").split(',')
if sex == '':
    what(name, city)
else:
    what(name, city, sex)


# 4、定义一个函数，成绩作为参数传入。如果成绩小于60，则输出不及格。
# 如果成绩在60到80之间，则输出良好；如果成绩高于80分，则输出优秀，如果成绩不在0-100之间，则输出 成绩输入错误。
def mark(score):
    score = int(score)
    if score < 60:
        print("不及格")
    elif 60 <= score <= 80:
        print("良好")
    elif 80 < score <= 100:
        print("优秀")
    else:
        print("输入错误")


mark(input("请输入成绩"))
