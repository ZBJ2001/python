'''
普通函数
    参数
    返回值
    作用
    闭包
    装饰器
匿名函数
    1、函数体非常简单
    2、使用次数较少
    作用：简化函数定义，使用方法。
    定义格式：关键字：lambda
        lambda 参数：返回值
    lambda 参数1，参数2... ：运算
高阶函数
    map()
    reduce()
    filter()
    max(key)
    min(key)
    sorted(key)


递归函数

'''


# 匿名函数练习 一个参数


def calc(n):
    return n + 1


f = lambda n: n + 1
print(f)

r = f(5)
print(r)
# 两个参数
f1 = lambda a, b: a + b
print('f1:', f1(3, 4))

# 直接使用
print((lambda a, b: a + b)(3, 5))


# 匿名函数作为参数
def test1(x, y, func):
    print(x, y)
    print(func)
    print('func(x,y)', func(x, y))


test1(5, 6, f1)
test1(7, 8, lambda x, y: x * y)
test1(7, 8, lambda x, y: x + y)
exit()
# 求最大值
list1 = [3, 5, 8, 9, 10]
m = max(list1)
print('{}的最大值{}'.format(list1, m))

list2 = [{'a': 10, 'b': 20}, {'a': 13, 'b': 20}, {'a': 9, 'b': 20}, {'a': 8, 'b': 20}]  # 找a里面的最大值。
print((lambda x: x['a'])(list2[0]))

print(max(list2, key=lambda x: x['a']))  # 这里是有迭代，把元素逐一传入lambda


def funls1(a):
    return a['a']


print(max(list2, key=funls1))  # 功能同上

# map函数 map(func, *iterables) --> map object
# map() 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

list1 = [3, 4, 5, 8, 9, 9, 0, 2, 3, 5]
result = map(lambda x: x + 2, list1)  # 把迭代的元素逐一传入函数中，操作一次，然后返回。

print(list(result))
print(list(enumerate(list1)))  # enumerate常用函数

# 复杂lambda表达式 带else
func = lambda x: x if x % 2 == 0 else x + 1  # 如果整除0，返回x,否则返回x+1
print(func(5))
result = map(func, list1)
result = map(lambda x: x if x % 2 == 0 else x + 1, list1)
print(list(result))

# lambda x: x if x % 2 == 0 else x + 1 等同于
for index, i in enumerate(list1):  # 直接产生序号和值。要不然需要在循环里加一个索引变量。
    if i % 2 != 0:
        list1[index] = i + 1

# reduce()
# reduce() 函数会对参数序列中元素进行累积。
# 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
# 用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
# 得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
from functools import reduce

print('{}依次相加{}'.format(list1, reduce(lambda x, y: x + y, list1)))

result = reduce(lambda x, y: x + y, (2,))  # 只有一个参数时，另一个参数为0.
print(result)
result = reduce(lambda x, y: x + y, (2,), 10)  # y是空时，用10这个默认值。如果减法，10会赋值给X.
print(result)

# filter
# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中。

list1 = [12, 6, 8, 98, 34, 36, 2, 8, 0]
#返回伟
list2 = filter(lambda x:x>10,list1)
print(list(list2))

list2 = [{'a': 10, 'b': 20}, {'a': 13, 'b': 20}, {'a': 9, 'b': 20}, {'a': 8, 'b': 20}]
list3 =  filter(lambda x:x['a']>=10,list2) #过滤出大于等于10的。
print(list(list3))



exit()


# 字典
def func(x):
    return x[1]

#排序  sort()
list3 = [('zbj', 40), ('zx', 17), ('zyr', 7)]
list4 = sorted(list3, key=lambda x: x[1], reverse=False)

print(list4)
list4 = sorted(list3, key=func)
print(list4)

exit()

def func(f):
    r = f(5)
    r += 10
    return r


func(lambda x: x * 2)
