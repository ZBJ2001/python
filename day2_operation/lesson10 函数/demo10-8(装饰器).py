'''
装饰器功能 decorator
    1、引入日志
    2、函数执行时间统计
    3、执行函数前的预备处理
    4、执行函数后清理 功能
    5、权限校验等场景
    6、缓存

# 装饰器功能函数
    1、@func  # 调用func函数 参数是buy_ticket
    2.执行函数体中内容
    3.加载内部函数
    4 返回内部函数wrapper.
    5、buy_ticket接收了func的返回值。


装饰器和闭包的区别？
   函数名=装饰器函数(函数名）

'''

def decorate(func):
    a = 100
    def wrapper():
        print('1111111111')
        func()
        print('2222222222')

    return wrapper

@decorate
def house():
    print('house')

house()
house()
# exit()


# 定义函数,闭包的原则
def func(f):
    print('------------>1')

    def wrapper():
        print('装饰前.......验证是否登录')
        f()
        print('装修后......')

    print('---------->2')
    return wrapper


# 功能函数
@func  # 调用func函数 参数是buy_ticket 2.执行函数体中内容 3.加载内部函数 4 返回内部函数wrapper.5。buy_ticket接收了func的返回值。
def buy_ticket():
    print('我可以买票去看:哪吒')


# 买票
buy_ticket()



# 装饰器函数
def decorator(func):
    def warapper():
        func()
        print('刷漆')
        print('铺地板')
        print('买家俱')
        print('可以住了')

    return warapper


@decorator #@后的函数名就是用这个函数装下面的函数。即对现有的函数的功能扩展。
def house():
    print('空毛坯房...')


house() #现在的house执行的已不是定义的代码了。而是执行装饰器函函数代码了！





#计数器
def decorator(func):
    count = 0

    def wrapper(*args,**kwargs):
        nonlocal count
        func(*args,**kwargs)
        count += 1
        print('第{}次调用函数{}'.format(count,func.__name__))

    return wrapper



#装饰 一个装饰器同时装饰多个函数。

@decorator
def show():
    print('正在使用show函数......')

@decorator
def test(n):
    print('------------->调用test函数',n)

@decorator
def test1(a,b=8):
    print('------------->',a,b)

def test2():
    print('---------->test2 function')


def test3(a,b):
    print('test3----------a,b',a,b)

show()
show()
test(6)
test1(a=5,b=10)

#以下代码等于装饰器功能。@decorator
test2 = decorator(test2)
test2()

test3 = decorator(test3)  #之所以不行，是因为test3()在闭包内部调用时，是需要函数的。
test3()
