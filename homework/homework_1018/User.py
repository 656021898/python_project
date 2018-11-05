# 1：创建一个名为 User 的类：
# 1）其中包含属性 first_name 和 last_name，还有用户简介通常会存储的其他几个属性，均是自定义， 请放在初始化函数里面。
# 2）在类 User 中定义一个名为 describe_user()的方法，它打印用户信息摘要；
# 3）再定义一个名为 greet_user()的方法，它向用户发出个性化的问候。:
# 请创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。

class User:

    def __init__(self,first_name,last_name,sex="男",age=25):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age

    def describe_user(self):
        print("姓名：{0}·{1}".format(self.last_name,self.first_name))
        print("性别：{0}".format(self.sex))
        print("年龄：{0}".format(self.age))

    def greet_user(self):
        print("hello,{0}·{1},欢迎你来到柠檬班！".format(self.last_name,self.first_name))


