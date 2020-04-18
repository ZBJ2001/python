'''
1、Import random 导入模块
2、加载函数 有内存地址
3、print(函数名不带括号） 打印函数地址
4、调用函数：函数名() 表示调用函数
'''
# 定义函数： 随机数的产生


import random


def generate_random(number): #形参：形式上的参数
    '''
    产生随机数
    :return:
    '''
    for i in range(number):
        ran = random.randint(1,20)
        print(ran)

def add(a,b):
    return a+b



def max(iterable):
    max = iterable[0]
    for i in iterable:
        if i > max:
            max=i
    return max

print('最大值是：',max([1,2,3,4]))
list
list1 = [12,3,4,5]
list1.reverse() #返转列表
print('反转',list1)
type(list1) #只能看到是什么类型，但不能在IF里进行判断 用isinstance()
if isinstance(list1,list):
    print('is list')



sum = add(3,4)
print(sum)
#调用
number = 5
generate_random((number)) #实参：实际的参数 ，具体的值。
#print(generate_random) #打印函数名
