'''
高阶函数
    把函数当成参数进行传递的函数。
    1、sorted(iterable,key,reverse) 其中的key就是一个函数参数。
    2、map()

    3、filter(function，iterable):返回值是一个filter object
    需要对返回值进行转换 list(filter_object)
    function函数的返回值必须是是booL类型。

    functools包
    4、reduce() #数字运算相关
    5、partial 偏函数。

'''
from functools import reduce
from functools import partial,wraps



# 按照字典的某一部分排序
dict1 = {'zbj': 90, 'ls': 100, 'ww': 89, 'zl': 92}
result = sorted(dict1.items(), key=lambda x: x[1])  # 关键是要知道变量X取的值是什么，并且是可迭代的。
dict1 = dict(result)
print(dict1)

# map 映射

result = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(list(result))

list1 = ['zbj', 'km', 'zx', 'zyr']

result = map(lambda x: x.title(), list1)
list2 = list(result)
print(list2)

# 找出偶数
numbers = [-1, 0, 1, 3, 5, 6, 3, 55, 5, 22]

f1 = filter(None, numbers)  # 0 当成假。 None位置如果放函数必须返回布尔值。
print(list(f1))
f1 = filter(lambda x: x % 2 == 0, numbers)
print(list(f1))

# 过滤出数字
list1 = ['hello', 30, '80', 50, 'he100', 'yes']
f1 = filter(lambda x: isinstance(x, int), list1)
f1 = filter(lambda x: str(x).isdigit(), list1)
print(list(f1))

students = [('tom', 20), ('luck', 18), ('jack',22)]
filter4 = filter(lambda x:x[1]>20,students)
print(list(filter4))