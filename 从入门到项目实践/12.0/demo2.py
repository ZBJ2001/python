# _*_ coding: UTF-8 _*_
# 开发团队 ：万宝软件部
# 开发人员 ：Administrator
# 开发时间 : 2020-8-5 22:55
# 文件名称 : demo2.py
# 开发工具 : PyCharm
# 任    务 ：面向对象学习
# 知 识 点 ：

class Geese:
    '''大雁类'''
    neck = "脖子较长"
    wing = "振翅频率高"
    leg = "腿位于身体的中心支点，行走自如"

    def __init__(self):
        print('我是大雁类！我有以下特征：')
        print(Geese.neck)
        print(Geese.wing)
        print(Geese.leg)


wildGoose = Geese()
