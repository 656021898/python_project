# 3.人和机器猜拳游戏写成一个类，有如下几个函数：
# 1）函数1：选择角色1 曹操 2张飞 3 刘备
# 2）函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
# 3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
# 4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
# 5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束
import random


class Game:
    dict_role = {"曹操": 1, "张飞": 2, "刘备": 3}
    dict_guess = {"剪刀": 1, "石头": 2, "布": 3}
    ping = 0
    user_win = 0
    user_lost = 0

    def role(self):
        while True:
            role_name = input("角色有：曹操、张飞、刘备，请输入角色名称：")
            if role_name not in self.dict_role.keys():
                print("输入的角色名称有误！")
                continue
            else:
                break
        return role_name

    def role_guess(self, role_name):
        while True:
            guess_name = input("{0}，请输入剪刀、石头、布：".format(role_name))
            if guess_name not in self.dict_guess.keys():
                print("输入的数据有误")
                continue
            else:
                guess_num = list(self.dict_guess.values())[list(self.dict_guess.keys()).index(guess_name)]
                break
        return guess_num

    @staticmethod
    def auto_guess():
        auto_num = random.randint(1, 3)
        return auto_num

    def fight(self):
        role_name = self.role()
        while True:
            guess_num = self.role_guess(role_name)
            auto_num = self.auto_guess()
            guess_name = list(self.dict_guess.keys())[list(self.dict_guess.values()).index(guess_num)]
            auto_name = list(self.dict_guess.keys())[list(self.dict_guess.values()).index(auto_num)]
            if (guess_num - auto_num) in [-2, 1]:
                self.user_win += 1
                print('电脑出：{0}      {2}出：{1}      结果：你赢了。'.format(guess_name, auto_name, role_name))
            elif (guess_num - auto_num) in [-1, 2]:
                self.user_lost += 1
                print('电脑出：{0}      {2}出：{1}      结果：你输了。'.format(guess_name, auto_name, role_name))
            else:
                self.ping += 1
                print('电脑出：{0}      {2}出：{1}      结果：平局。'.format(guess_name, auto_name, role_name))
            my_continue = input('继续输入是，退出输入否')
            if my_continue == 'y':
                continue
            elif my_continue == 'n':
                break
        print('{0}一共玩了{1}局，你赢了{2}局，输了{3}局，平了{4}局，游戏结束！'.format(role_name, (self.user_win + self.user_lost + self.ping),
                                                               self.user_win,
                                                               self.user_lost, self.ping))


Game().fight()

