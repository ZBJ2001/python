'''
图书管理系统
'''

#用户注册
def register():
    username = input('输入用户名：')
    password = input('输入密码：')
    repassword = input ('输入确认密码：')

    if password == repassword:
        #保存信息
        with open('e:/p1/users.txt','a') as wstream:
            wstream.write('{} {}\n'.format(username,password))
        print('用户注册成功！')
    else:
        print('密码不一致')


#用户登录
def login():
    username = input('输入用户名：')
    password = input('输入密码：')
    if username and password: #都不是空
        with open('e:/p1/users.txt') as rstream:
            while True:

                user = rstream.readline() #读一行 admin 123\n
                if not user:
                    print('用户名或密码输入错误！')
                    break
                input_user = '{} {}\n'.format(username,password)
                if user == input_user:
                    print('用户登录成功！')
                    break


def show_books():
    print('-----------------------图书列表---------------------')
    with open('e:/p1/books.txt') as rstream:
        books = rstream.readlines()
        for book in books:
            print(book,end='')

#register()
#login()
show_books()