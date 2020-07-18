'''
    装饰的函数有返回值


    #这里的f3就是wrapper,所以，wrapper的参数要和原F3一致，否则只能按wrapper函数的参数进行调用了。
# 但按wrapper调用时，其wrapper内部调用原来的f3,也是需要参数的。所以这样就要求wrapper的参数和被装饰的函数参数必须一致了。

'''

#万能装修器，能装修多个参数（*args,**kwargs)

def decorate_more(func):
    print('装饰前执行...')
    def wrapper(*args,**kwargs):
        print('正在装饰中...')
        func(*args,**kwargs)
        print('装饰完毕...')
    return wrapper

def decorate_1(func):
    print('装饰前执行...')
    def wrapper():
        print('正在装饰中...')
        func()
        print('装饰完毕...')

    return wrapper


@decorate_more
def f1():
    print('--------f1()-------')

@decorate_more
def f2(n):
    print('--------f2(n)------')

@decorate_1
def f3(m,n):
    pass

def f4(**kwargs):
    pass


f1()
f2(2)
#这里的f3就是wrapper,所以，wrapper的参数要和原F3一致，否则只能按wrapper函数的参数进行调用了。
# 但按wrapper调用时，其wrapper内部调用原来的f3,也是需要参数的。所以这样就要求wrapper的参数和被装饰的函数参数必须一致了。
f3()
exit()

flag = False
#定义一个装饰器函数
def decorator(func):
    def wrapper(*args,**kwargs):
        print('-------------->进行用户登录验证')
        r = func(*args,**kwargs) #装饰器带返回值的
        if r:
            return 'scuesss'
        else:
            return 'fail'
         #同样要返回 被装修的函数有返回值，这也要返回。
    return wrapper

def login():
    global flag
    username = input('输入你的用户名：')
    password = input('输入密码：')
    if username=='admin' and password == '123':
        flag = True


@decorator
def islogin():
    if flag:
        return True
    else:
        return False

login()
r = islogin()
print('---------->',r)


