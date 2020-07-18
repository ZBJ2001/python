'''
图书管理
    1、借书
    2、还书
    3、查询书籍
    4、打印所有书籍
    5、退出系统
    books=[[书名，数量],[书名，数量],[书名，数量],[书名，数量]]
    database=
    [[姓名，所借书籍{}],[姓名，所借书籍{}]]
'''
import time

print('*' * 50)
print('------------------千锋图书馆-----------------------')
print('*' * 50)

# 图书管书定义
books = [['防脱发指南', 5], ['颈椎康复指南', 3], ['python从入门到精通', 6], ['活着', 4], ['追妹指南', 4]]
# 学生借书容器
student_books = []
from  assignment1 import my_align
print (my_align('zbj',10,'L'))
print (my_align('张宝军',10,'L'))

while True:

    choice = int(input('请选择功能：1.查询书籍 2.借书 3.还书 4.显示所有书藉 5.退出系统'))
    if choice == 1:
        #查询书
        print('------------------------------')
        search_book = input('请输入要查询的书籍名称：')
        #遍历BOOKS
        for book in books:
            if search_book in book:
                print('查询的书籍名称是{}，可借数量{}'.format(book[0],book[1]))
                break
        else:
            print('查无此书')

    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        #显示所有书藉
        print('------------------图书馆所有书籍如下：---------------------')
        print('书名'.ljust(30,'-')+'数量')
        for book in books:
            print(my_align(book[0],30,'L'),book[1])
    elif choice == 5:
        answ = input('确定要退出图书管理系统吗？(y/n)')
        if answ.lower() == 'y':
            print('即将退出系统......')
            time.sleep(1)
            print('系统关闭，欢迎下次使用')
            break

    else:
        print('输入错误，重新输入！')

