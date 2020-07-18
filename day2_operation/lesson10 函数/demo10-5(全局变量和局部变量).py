'''
作用域
legb
local 局部的
enclosing 嵌套的 闭包
global 全局的 在函数中对全局变量进行声明而使用的。
builtins 系统内置的

全局的 global
外层函数的 nonlocal
nonlocal n #只要是内部，需要改外部，用nonlocal 访问是不需要的。
nonlocal n #只要是内部，需要改外部，用nonlocal 访问是不需要的。主要是针对不可变变量。
global b #在内部函数中用全局的，用global. 主要是针对不可变变量

全局也分可变不可变。
可变类型不需要global

locals()在函数中使用，获取的是当前函数的局部变量位。
globals()用在函数的外层，获取全局的变量

搜索变量的规则是：
1、如果有内部函数，先找内部函数自身的变量
2、如果内部函数自身没有变量，则找外部函数的变量
3、如果外部函数也不存在此变量，则找全局
4、如果全局也没有此变量，则找builtins
5、如果builtins也没有，则报错。

问题：
1、全局变量函数可以访问，但不能修改。但目前这个版本是可以修改的？需要落实。
    落实结果：
    内部函数是起作用的。注意，是内部函数。普通函数是用不到的。
    全局的 global
    外层函数的 nonlocal
知识点：
1、enumerate(list)
'''

wbstr = 'zbj'
list1 = [1, 2, 3, 4, 5]
i = 2


def func1():
    s = 'abce'
    s += 'x'
    wbstr = 'km'

    # global i
    list1.append(6)
    list1[0] = 8
    print(list1)
    print(s, wbstr)

    def func2():
        i = 3
        print(i)

    func2()


# func1()
b = 500
listgloabl = [50,60,70,80]
def out_func():
    # 声明变量
    n = 100
    a = 1
    list1 = [3, 6, 9, 4]

    def inner_func():
        nonlocal n #只要是内部，需要改外部，用nonlocal 访问是不需要的。主要是针对不可变变量。
        global b #在内部函数中用全局的，用global. 主要是针对不可变变量
        listgloabl.append(1000)
        listgloabl[0] = 10
        list1[0] = 20
        list1.append(50)
        for index, i in enumerate(list1, start=1):
            print(index, i)
        for index, i in enumerate(list1):
            list1[index] = i + 5
        list1.sort()
        n += 1
        print(a)
        b = b+1
    print(locals()) #发前函数的局部变量 字典形式。
    print(globals()) #模块的全局变量 字典形式
    inner_func()


out_func()
exit()

number = 10  # 全局变量


def func():
    # number = 0 #局部变量
    global number  # 如果想修改全局的变量，必须要明确声明。
    print(number)
    for i in range(number):
        print('----->', i)
    number = 9  # 相当于修改全局变量 number
    number += 5  # 函数只能修改自身的变量。可以读上一层的。


# func()
# print(number)

books = ['1', '2', '3', '4']


def func1():
    global books  # 这个global可以省略。
    books.append('5')
    a = 100
    b = 200
    print('------->:', books)
    print(locals())


# func1()
# print(books)
# print(globals())
# print(locals())

# 内部函数
a = 200  # 全局变量


def funmain():
    a = 10  # 相对于内部，这个是外部函数的局部变量
    b = 'good'
    c = [12, 3, 4, 5]

    def inner_fun():  # 内部函数
        a = 100  # 内部函数的局部变量。
        print('我是一个内部函数！')

    # 调用内部函数
    inner_fun()
    print(locals())

    # 返回值，结束函数
    return a


# r = funmain()
# print(r)


def func(b):
    a = 10

    def inner_func(c):
        nonlocal b
        c = a + b + c
        b = c
        print('a:', a)
        print('b:', b)
        print('c:', c)

    inner_func(5)


# func(8)

set1 = {1, 3, 4, 5}
list1 = [1, 3, 4]


def func(pset, plist):
    plist.append(5)


func(set1, list1)
print(set1, list1)
