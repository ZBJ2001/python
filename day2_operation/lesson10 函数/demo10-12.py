#开发：登录验证
import time

islogin = False #默认是没有登录的。

def login():
    username = input('输入用户名：')
    password = input('输入密码：')
    if username =='admin' and password=='123456':
        return True
    else:
        return False


#定义装饰器，进行付款验证
def login_required(func):
    def wraaper(*args,**kwargs):
        global islogin
        #验证用户有没有登录。
        print('----------付款------------')
        if islogin:
            func(*args,**kwargs)
        else:
            #跳转到登录页面
            print('用户没登录,不能付款')
            islogin = login()
            print('result:',islogin)


    return wraaper


@login_required
def pay(money):
    print('正在付款，付款金额是：{}元'.format(money))
    print('付款中....')
    time.sleep(2)
    print('付款完成！')


pay(10000)
pay(8000)
