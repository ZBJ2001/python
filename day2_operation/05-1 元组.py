'''
元组：
    特点：
    类似列表，但不支持删除，添加和修改
    支持下标和切片
    元组的内置函数：
        本身不支持填加和删除和修改的。
        只能借助元组转列表，操作后，转换为元组。

    tup1 = () #空元组
    tup2 = (1,) #有一个元素的元组

    支持：
    查找：index() 查找对应的值，如果找不到，返回错误.返回第一个找到的。如果有第二个，忽略
    查找个数：count() 返回某个值出现的次数
    排序：
        系统提供的sorted 默认方法排序。返回是一个列表类型
        print(sorted(list2,reverse=True)) #降序
        print(sorted(list2)) #升序
    类型的转换
    list<--->tuple
    tuple(list) 得到元组类型
    list(tuple) 列表类型

    max()
    min()
    sum()
    len()
    +:两个元组可以相加
    *：可以相乘。 复制元组
    in:
    is:
    补充：声明含有一个元素的元组： （1，）加上一个逗号。

    任意无符号的对象，以逗号隔开，默认为元组
        x, y = 1, 2
    ：
c 是class
v是变量
f是function

排序的三种方式
1、sorted（list1,reverse = True) 降序
2、list1.sort(reverse = True) 对列表直接排序
3、list1.sort() 升序排列，list1.reverse() 返转

拆包和装包

'''
#拆包和装包

def fun5():
    a,b = (4,7)
    #变量个数与元组个数不一致时？
    b,*a = 2,4,8,9 #默认为元组。等同于（2，4，8，9）
    print(a)
    a,*b = (1,) #b是空列表。 *b表示未知
    print(b)
    (*b,) = (1,2,3) #元组对元组才可以
    a,*b = [1,2,3]
    *b, = 1,23

    print(b,*b) #有*号，拆包。 b是装过包的，*b就是拆包的。
    x,y,*z = 'hello'
    print(x,y,z,*z)
    print(*[4,8,6])
    print(*(1,3,4))
    print(*'zbj')
    print(*{3,5,7})
    print(*{1:'zbj',2:'km'})

    #赋值 * 是装包 输入 形参就是输入，所以输入一系列数会装成元组。
    #打印 * 即拆包。输出

fun5()
exit()

## 元组的新建，增删改查 切片
def func1():
    tup1 = ()  # 空元组
    tup2 = (1,)  # 有一个元素的元组
    tup3 = (2)  # 单独一个按元素的类型算了。
    tup4 = ('zbj')
    print(type(tup2), type(tup3), type(tup4))
    tup1 = (1, 2, 3, 4, 5, 6)
    print('{}tup1[1:3]'.format(tup1), tup1[1:3])  # 下标不包括3.只有1，2


def func2():
    tup1 = (1, 2, 3, 4, 5)
    print('tup1.index(2)',tup1.index(2))


func2()
exit()
list2 = [1, 2, 3, 4, 5, 6]
tuple2 = (1, 3, 5, 7, 9, 3)
print(type(list2))
print(type(tuple2))
tuple3 = tuple2
print(tuple3[::-1])  # 切片 倒序输出
print(tuple3.index(3))  # 查找对应的值，如果找不到，返回错误
print(tuple3.count(3))
print(sorted(tuple3))  # 默认方法排序。返回是一个列表类型
print(sorted(list2, reverse=True))  # 降序
print(tuple(sorted(list2)))  # 升序

tuple3 = (1,)  # 只有一个元素时，必须要用，要不然不是元组类型。
tuple3 += (3, 4)
print(tuple3)
