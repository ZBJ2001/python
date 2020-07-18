'''
无参数函数
    def func(): pass

    func()
有参数函数
    1、普通参数 形参实参个数要一致。
        def func(name,age):pass

        func('zbj',45)

    2、可变参数
        参数个数可以没有，也可以是多个。
        一个*的，不能是关键字参数。
        两个*，必须是关键字参数。
        def func(*args): pass

        func(1,2,3,5....)
        func(*(1,2,3,4))
        func(*[1,2,3,4])

        关键字可变参数
        def func(**kwargs):pass

        func(a=1,b=2,c=3)
        func(**{'a':1,'b':2,'c':3})
    3. 拆装包的活用。
        def func(*args,**kwargs): pass

    4.混用
        def func(已知放前，不确定放后，关键字最后）
        def func(nage,*args,**kwargs)


关键字参数 即默认参数
    key=value
    add(a=1,b=2)
    add(a,b=10)
    add(a,b,c=5)

    如果可变参数和关键字参数一起使用，关键字参数放最后更合理一些？也不是？其实关键字参数最好是明确赋值，如sep='/',
    放到最后是最合理和方便使用的。



不定长参数 可变参数
    带*即可变参数 传值为1，2，3，4，5
    *args 是习惯
    **kwargs 传值是a=1,b=2,c=3 ...不定长。类似关键字参数，只是关键字参数数量是一定的。这个是可变的。
    可变参类型是tuple 元组。
    传参数要是拆包的参数。如果是list或tuple前面要加上* 才可以实现拆包

    列表也可以拆
'''
#
# list1 = [1, 2, 3]
# n1, n2, n3 = list1  # 都会先做拆包的动作。其次再给前面变量赋值。
#
# list2 = [1, 2, 3, 4, 5, 6, 7]
# x, y, *z = list2 #自动把后面的3，4，5，6，7装包为list赋给Z.
# a,*b,c = list2
# print(a, b, c)


def bb(a,b,*c,**d):
    print(a,b,c,d)

bb(1,2)
bb(a=1,b=2)
bb(1,2,3,4,c=1,d=2)


exit()
def func(**kwargs):
    print(kwargs)

func(a=1,b=2)
func(**{'a':1,'b':2}) # 这里是传入参数前的使用，即拆包。传到参数里，遇到**即装包。


students = {'001':('zbj',45),'002':('zx',17),'003':('zry',8)}


def print_boy(persons):
    if isinstance(persons,dict):
        for name,age in persons.values():
            print(name,age)

#print_boy(students)
def print_boy2(name,**kwargs):
    if isinstance(kwargs,dict):
        for name,age in kwargs.values():
            print(name,age)

print_boy2('zbj',**students)
exit()

def add3(name,age=10,*args):
    print(name,age)
add3('zbj',age=10,)
exit()


def add(a,b=10): #关键数参数
    result = a+b
    print(result)

add(5)
add(4,7)
add(a=1,b=2) #关键字赋值 明确哪个参数赋哪个值。

def add1(a,b=10,c=4):
    result = a+b+c
    print(result)

add1(1)
add1(2,c=5) #关键字赋值






# pack 装包。unpack 拆包
def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)


print()
def join(seq,*args):
    s = ''
    print('len:',len(args))
    for i in args:
        s += i

        s += seq
    s = s[:-1]
    print('-------->',s)


def func1(*args,**kwargs):
    print(args)
    print(kwargs)


list1 = [1,2,3,4,5]
func1(list1)
tup1 = (1,2,3,4)
func1(tup1)
func1(*list1,10) #func(1,2,3,4,5,10)
func1(a=1,b=2)

students = {'zbj':44,'zx':17,'zyr':7}
def func(age,student):
    for key,value in student.items():
        if value < age:
            student[key] = value +1

func(20,students)
