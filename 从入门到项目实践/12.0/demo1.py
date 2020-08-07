# _*_ coding: UTF-8 _*_
# 开发团队 ：万宝软件部
# 开发人员 ：Administrator
# 开发时间 : 2020-8-5 22:34
# 文件名称 : demo1.py
# 开发工具 : PyCharm
# 任    务 ：面象对象学习
# 知 识 点 ：

class Ta:
    def __init__(self):

        print('Ta类的构造函数')
    def afunc(self):
        self.临时加的变量1 = 10
        print(self.临时加的变量1) # 这里调用的实例属性，调用时还没有，就是空吧!
    def afunc2(self):
        print(self.临时加的变量1)
class Taa(Ta):
    def func1(self):
        print('Taa类的fun1函数')


class Tab(Ta):
    def __init__(self):
        print('Tab类的构造函数')


a = Ta()
aa = Taa()
ab = Tab()

#a.临时加的变量1 = 100
#a.临时加的变量1 = 200
a.afunc()
a.afunc2()


class Geese:
    '''大雁类'''
    def __init__(self,beak,wing,claw):
        print('我是大雁类！我有以下特征：')
        print(beak)
        print(wing)
        print(claw)

beak1 = "喙的基部较高，长度和头部的长度几乎相等"
wing1 = "翅膀长而尖"
claw1 = "爪子是蹼状的"
wildGoose = Geese(beak1,wing1,claw1)
