import random
import assignment1


# 声音变量

assignment1.printXushu()
#assignment1.caicaile()
exit() #退出当前程序
count = 0
while (count < 3):
    username = input('输入用户名：')
    password = input('输入密码：')
    # admin 123456 默认
    if username == 'admin' and password == '123456':
        print('登录成功！')
        break  # 结束循环
    else:
        print('用户名或者密码有误！')

    count += 1
else:
    print('超过三次，账户锁定')

for count in range(0, 5):
    print(count)


choice = int(input('请选择需要办理的功能（1.办卡 2.存钱 3.取钱 4 修改密码 5.解锁 6。转帐 7.退出：'))
if choice == 1:
    pass  # 关键字
    print('办卡功能：')
    d1 = random.randint(0, 9)  # 随机整数
    d2 = random.randint(0, 9)  # 随机整数
    d3 = random.randint(0, 9)  # 随机整数
    card = str(d1) + str(d2) + str(d3)
    print('您的卡号：%s' % card)
elif choice == 2:
    pass
    print('存钱功能：')
elif choice == 3:
    print('取钱功能：')
elif choice == 4:
    print('修改密码功能：')
elif choice == 5:
    print('解锁功能：')
elif choice == 6:
    print('转帐功能：')
elif choice == 7:
    print('系统退出：')
else:
    print("输入有误，重新输入")
