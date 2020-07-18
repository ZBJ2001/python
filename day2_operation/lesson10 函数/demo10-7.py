'''
函数做为参数
闭包就是能够读取其他函数内部变量的函数


闭包实例
'''
from collections import Iterable
import types

books = [1,2,3,4,5,5]

def func1 (books):
    if isinstance(books,Iterable):
        for book in books:
            print(book)
#func1(books)

def A():
    print('hello world')

def func2(f):
    print('------->',f)
    if callable(f): #判断变量是不是函数
        f()  # 调用函数参数
        print('yes funciton')
    if isinstance(f,types.FunctionType):
        print('types.FunctionType is True')
func2(A)


def func3(a,b):
    print('func3 sum is :',a+b)
f1 = func3
f2 = func3

f2(2,3)
f1(1,2)

#闭包的同级访问。
def func():
    c= 100
    def inner_func1():
        print('hello inner_func1')
    def inner_func2():
        inner_func1()
        return 'hello'
    return inner_func2

#func2(A)


#计数器
def generate_count():
    container = [0]

    def add_one():
        container[0] += 1
        print('当前是第{}次访问'.format(container[0]))
    return add_one

#内部函数是一个计数器。外部变量一直保存着，所以可以共享操作。
counter = generate_count()
counter()
counter()
counter()
