# _*_ coding: UTF-8 _*_
# 开发团队：万宝软件部
# 开发人员： Administrator
# 开发时间 : 2020-7-20 18:35
# 文件名称 : demo4.py
# 开发工具 : PyCharm
# 任   务  :
# 学习要点 :
# 知 识 点 ： chr(),ord()，print(),open(),datetime().now().year,format()
# 编码规范
'''
1、import 一次只导入一个模块
2、行尾不用分号
3、字符串每行超过80，用（），表达式多行表示用\
'''

import datetime
print(chr(97))
print('a')
print(ord('a'))
print(chr(7),chr(42),chr(38))

print(hex(ord('张')),'\u5f20',ord('张'))

#print()输出到文件
fp=open(r'e:\mr.txt','a+')
print('要么出众,要么出局',file=fp)
fp.close()

print('当前年份:{0}'.format(datetime.datetime.now().year))


#根据输入年份，计算年龄
imyear = input('请输入您的出生年份：')
nowyear = datetime.datetime.now().year
age = nowyear-int(imyear)
print('您的年龄为：'+str(age)+'岁')

if age < 18:
    print('您现在为未成年人 ~@_@~')
if 66>age >= 18:
    print('您现在为青年人 （-_- )')
if 80 >age >= 66:
    print('您现在为中年人 ~@_@~')
if age >= 80:
    print('您现在为老年人')



#编码规范
print('asdfasdfasdfsadfsadf'
      'adsfasdfsadfsdaf')
print('asdfasdfasdfasdf\
3333333333')