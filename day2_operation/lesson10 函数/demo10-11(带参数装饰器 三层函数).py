'''
多层装饰器
    @装饰器2
    @装饰器1
    def func()被装饰函数
    先执行1，再执行2.谁近先执行谁。

装修器带参数
    是三层函数实现
    第一层是装饰器名，接收装饰器参数
    第二层 和正常的一样。会一层一层的执行。

    谁离原函数最近，先执行哪个装饰器部分。
    将第一个执行装饰器的返回值第二个装饰器。
'''

#装饰器带参数实现 还有些没理解透。?
def decorator(number):
    print('第一层')
    def dec1(func):  #第二层
        print('第二层')
        def wrapper(*args,**kwargs): #第三层
            print('第三层')
            print('---->start')
            func(*args,**kwargs)
            print('------>end')
        return wrapper
    return dec1

@decorator(10) #装饰器传递参 这里等于先执行了两步。 将函数返回给def_show

def def_show():
    print('--->调用show函数！')


# def_show()
# exit()
#可以这样理解
#def_show = decorator(10)(def_show)

def_show()
exit()

#多层装饰器实现

def zhuang1(func):
    print('------------>1 start')
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        print('刷漆')
    print('------------>1 end')

    return wrapper

def zhuang2(func):
    print('------------>2 start')
    def wrapper(*args,**kwargs):

        func(*args,**kwargs)

        print('铺地板，装门')
    print('------------>2 end')

    return wrapper

@zhuang2
@zhuang1
def house(a):
    print('我是毛坯房')


house(1)

exit()
#多层装饰器的理解
house = zhuang2(zhuang1(house))
