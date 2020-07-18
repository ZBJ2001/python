'''
购票系统装饰器
'''

islogin = False
#定义一个装饰器函数
def login_required(func):
    def wrapper(*args,**kwargs):
        global  islogin
        if islogin:
            func(*args,*kwargs)
        else:
            print('---->用户还没有登录，请登录！')
            f = login()
            if f:
                func(*args,**kwargs)

         #同样要返回 被装修的函数有返回值，这也要返回。
    return wrapper

def login():
    global  islogin
    username = input('输入你的用户名：')
    password = input('输入密码：')
    if username=='admin' and password == '123':
        islogin = True
        return True

    else:
        islogin




@login_required
def buy_ticket():
    ticket={'中影星美水城店':('哪吒',['11:35 1号厅','12:55 3号厅','14:08 1号厅']),
            '奥斯卡':('西游记',['11:35 1号厅','12:55 3号厅','14:08 1号厅']),}
    for key ,value in ticket.items():
        print('影院:',key)
        print('播放的电影是:',value[0])
        print('播放的时间是:')
        for i in value[1]:
            print('-->',i)

buy_ticket()