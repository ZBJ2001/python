#学员信息在线管理
import os


#定义一个用于存放学员信息的变量 列表
stulist = [
    {'name':'张三','age':20,'classid':1},
    {'name':'李四','age':22,'classid':2},
    {'name':'王五','age':33,'classid':3},
    {'name':'张宝军','age':44,'classid':4},
    {'name':'杨童心','age':16,'classid':5}
]
#定义一个学员信息输出的函数
def showStu(stulist):
    '''
    标准注释
    :param stulist:
    :return:
    '''
    if len(stulist) == 0:
        print ("==================没有学员信息可以输出===============")
        return
    print("|{0:<5}|{1:<10}|{2:<5}|{3:<10}|".format("sid","name","age","classid"))
    print("-"*40)
    for i in range(len(stulist)):
        print("|{0:<5}|{1:<10}|{2:<5}|{3:<10}|".format(i+1, stulist[i]['name'], stulist[i]['age'], stulist[i]['classid']))

while True:

    #输出初始界面
    os.system("cls")
    print("="*12,"学员管理系统","="*12)
    print("{0:1}{1:13}{2:15}".format(" ","1.查看学员信息","2.添加学学员信息"))
    print("{0:1}{1:13}{2:15}".format(" ","3.删除学员信息","4.退出系统"))
    print("="*37)

    key=input("请输入对应的选择：")
    if key == "1":
        print ("="*12,"学员信息浏览","="*14)
        showStu(stulist)
        input ("换回车键继续")
    elif key == "2":
        print("="*12,"学员信息添加","="*14)
        input("换回车键继续")
    elif key == "3":
        print("="*12,"学员信息删除","="*14)
        input("换回车键继续")
    elif key == "4":
        print("="*12,"再见","="*14)
        break
    else:
        print ("="*14,"无效的键盘输入","="*14)