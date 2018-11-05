# 4：按照以下要求定义一个游乐园门票类，并创建实例调用函数，完成儿童和大人的总票价统计（人数不定，由你输入的人数个数来决定）
# 1.平日票价100元
# 2.周末票价为平日票价120%
# 3.儿童半价

import datetime
class Ticket:

    @staticmethod
    def data():
        dict_weekday ={0:"星期一",1:"星期二",2:"星期三",3:"星期四",4:"星期五",5:"星期六",6:"星期天",}
        price =100
        year,month,day = input('请输入年、月、日，格式为2018-5-10：').split('-')
        weekday_num = datetime.date(int(year),int(month),int(day)).weekday()
        weekday_name = dict_weekday.get(weekday_num)
        return weekday_num,weekday_name

    @staticmethod
    def total_price():
        price = 100
        weekday_num,weekday_name = Ticket.data()
        adult = int(input("请输入成人人数："))
        child = int(input("请输入儿童人数："))
        if weekday_num in [0,1,2,3,4]:
            print("今天为{0}，执行平日票价，{1}/人，您的总票价为：{2}".format(weekday_name,price,(adult*price+child*0.5*price)))
            return (adult*price+child*0.5*price)
        else:
            print("今天为{0}，执行周末票价，{1}/人，您的总票价为：{2}".format(weekday_name,price*1.2,(adult*price*1.2+child*0.5*price*1.2)))
            return (adult*price*1.2+child*0.5*price*1.2)

