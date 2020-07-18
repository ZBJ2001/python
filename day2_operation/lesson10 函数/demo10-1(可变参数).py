'''
可变参数,必须是函数形参的最后一个参数。
    def fun (*args)
    拆包和封包
关键字参数
    的默认值。key = value
    def fun (a=1,b=2,c=3)

    def fun(**kwargs): # key word argument 关键字参数 赋值:fun(a=1,b=2,c=3) 转成字典
    如果是参数是一个字典，需要转换为**字典

    1、*args
    2、name,*args 可变结合不可变，不可变的放前，可变的放后。
    3、name,age,*args

'''
def add1(*args):
    print(args)

#2有固定的和可变的混使用
def add(name,*args): #是个空元组
    sum = 0
    if len(args)>0:
        for i  in args:
            sum += i
        print('{}和是：{}'.format(name,sum))
    else:
        print('没有元素可计算')


add1(1,2,3)

exit()


def add1(a,b=10,c=4):
    print (a+b+c)

def fun1(**kwargs):
    print(kwargs)

fun1(a=1,b=2,c=3)

add1(10,c=6) #可以指定参数

#函数：打印每位同学姓名 和年龄
students = {'001':('张宝军',44),'002':('张潇',17)}
print(students['001'])
for stu in students: #这里迭代的是字典的KEY
    print(stu)

def print_boy(persons):
    if isinstance(persons,dict):
        for name,age in persons.values(): #这种语法很方便。
            print(name,age)


print_boy(students)
