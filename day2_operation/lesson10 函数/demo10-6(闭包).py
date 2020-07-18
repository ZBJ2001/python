'''
闭包 主要用于装饰器。
    1、必须是一个函数。并且是一个双层函数。在一个函数中定义了另一个函数。
    2、内层函数使用了外层函数的变量。不使用外部变量不是严格的闭包。
    3、返回值是内层函数名，不能加括号 。
    4、可以这样理解，每调一次外部函数，就重新声明一次内部函数，即产生不同的地址。所以，每调用一次，返回的地址不同。


闭包总结
    1、闭包优化了变量，原来需要类对象完成的工作，闭包也可以完成
    2、由于闭包引用了外部函数的局部变量，由外部函数的局部变量没有及时释放，消耗内存.同时，局部变量可以保留中间结果。
    3、闭包的好处，使代码变得简洁，便于阅读代码。
    4、闭包是理解装饰器的基础。
'''
import sys


def outer_func(n):
    a = 10
    print('------outer_func------')
    def inner_func():
        nonlocal a
        a +=1

        r = a + n
        print('r----->:',r)
        return 0
    print('------------内部查看地址',id(inner_func))

    return inner_func




result = outer_func(1)
#调用内部函数功能。
print(result(),id(result))
result()
result()

result2 = outer_func(1)
print(result2(),id(result2),id(outer_func))

# n= sys.getrefcount(outer_func)
# print('n------->',n)

# print(result.__closure__)


#带参数的闭包函数
def out_func2(a,b):
    c = 10
    def inner_func():
        print('相加之后的结果是：',a+b+c)
    return inner_func

#返回是内部函数的地址
result = out_func2(5,6)
#调用返出来的内部函数
result()