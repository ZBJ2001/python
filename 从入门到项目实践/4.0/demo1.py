# _*_ coding: UTF-8 _*_
# 开发团队 ：万宝软件部
# 开发人员 ：Administrator
# 开发时间 : 2020-7-20 22:11
# 文件名称 : demo1.py
# 开发工具 : PyCharm
# 任    务 ：
# 知 识 点 ：

i8 = 0o123
i16 = 0x25
i2 = 0b101
print(i8,i16,i2,oct(i8),hex(i16))
print('%o,%x' % (i8,i16))
print(int(i8))

tuple1 = range(10) #返回的是对象。

print(list(tuple1),type(tuple1))
for i in range(10):
    print(i)


print([i for i in range(10)])

import random
randomnumber = (random.randint(10,100) for i in range(10))
print(tuple(randomnumber))


def bun_bmi(person,height,weight):
    '''
    功能：根据身高和体重计算BMI指数
    person:姓名
    height:身高，单位：米
    weight:体重, 单位：千克

    '''
    print(person + '的身高：'+str(height))