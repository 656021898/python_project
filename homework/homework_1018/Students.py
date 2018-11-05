# 2：定义一个学生类。
# 1）有下面的类属性： 1 姓名 2 年龄 3 成绩（语文，数学，英语)[每课成绩的类型为整数] ,均放在初始化函数里面。
# 2）类方法：
# a)获取学生的姓名：get_name() 返回类型:str b)获取学生的年龄：get_age() 返回类型:int
# c) 返回3门科目中最高的分数。get_course() 返回类型:int
# 写好类以后，可以定义2个同学测试下: zm = Student('zhangming',20,[69,88,100]) 返回结果： zhangming 20 100

class Students():
    def __init__(self,name,age,course=[]):
        self.name = name
        self.age = age
        self.course = course

    def get_name(self):
        return self.name

    def get_age(self):
        return int(self.age)

    def get_course(self):
        self.course.sort()
        return self.course[-1]


