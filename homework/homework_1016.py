# -*_ coding:utf-8 _*-

class developer:

    work_year = 5
    def laguage(self,*aa):
        my_laguages = input("请输入语言").split()
        print('我会写:',end='')
        for my_laguage in my_laguages:
            if my_laguage is my_laguages[-1]:
                print(my_laguage)
            else:
                print(my_laguage,end='、')

    def year(self):
        print("我工作{0}年了".format(self.work_year))


huahua = developer()
huahua.laguage()
huahua.year()