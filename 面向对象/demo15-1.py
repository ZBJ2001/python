'''
面向对象

#类属性
    类属性用类名来操作
#对象属性
    自己的是对象属性。和类的属性可以重名.可以动态填加。

#类中的方法
    普通方法 def 方法名（self[,参数，参数]): pass
        对象调用方法时,会自动把对象本身当参数传到方法里.
    类方法
        @classmethod
        def test(cls): #类方法，传递参数是类
            pass
        类方法中只能使用类属性。
        类方法不能使用普通方法。因为没有SELF参数。

    静态方法
        很类似于类方法。
        1.需要装饰器@staticmethod
        2，没有类参数，也没有对象参数。
        3.类名.静态方法调用。
        4.也只能访问类的属性和方法。通过类名调用。
    魔术方法

#私有的前面加__
    私有属性，私有方法。


'''


class Phone:
    type = '7'

    # 魔术方法 前后带__就是魔术方法
    def __init__(self):  # init 初始的。这里初始的是对象的成员变量。如何保证每个对象都有成员变量呢？用__init__()
        print('------------init')
        self.brand = 'phone'
        self.price = 4999

    # 类里面的方法.
    def call(self):  # self是不断变化的，根据对象不同。
        print('正在打电话....')
        print('留言：', self.note)


class Student:
    name = 'zbj'
    age = 45


class Person:
    count = 0
    name = '张三'
    __age = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1
        print('Person类共生成{}个对象'.format(Person.count))

    def eat(self, food):
        print('{}正在吃{}!...'.format(self.name, food))
        print(Person.eat)
        self.run()  # 普通发法内部可以调用普通方法，用self调用。

    def run(self):
        print('{},今年{}岁,正在跑步'.format(self.name, self.age))

    @classmethod
    def update_age(cls):
        cls.__age = 20

    @classmethod
    def show_age(cls):
        print('修改后的年龄是：', cls.__age)

    @staticmethod
    def test():
        # 没有参数
        print('--------->静态方法')
        #可以用类名调用类的成员。

class Dog:
    __color = '黄色'  # 私有属性

    def __init__(self, nickname):
        self.nickname = nickname

    def run(self):
        print('{}在院子里跑来跑去！'.format(self.nickname))
        # 调用普通方法
        self.__eat()
        # 普通方法调用类方法
        Dog.test()

    def __eat(self):
        print("{}正在吃东西".format(self.nickname))

    @classmethod
    def test(cls):  # 类方法，传递参数是类  没有对象也可以使用。
        print(cls)

    @classmethod
    def test1(cls):
        Dog.test()  # 调用类方法
        Dog('mimi').run()  # 调用普通方法，即对象方法。


# zbj = Student()
# km = Student()
# km.name = 'km'
# print('zbj is addr is :{0}'.format(id(zbj)))
# print('km is addr is :{0}'.format(id(km)))
#
# print(id(zbj.name))
# print(id(km.name))
#
# Student.name = 'km'
# print(zbj.name)

phone1 = Phone()
phone1.note = '我是phone1的专有属性note'

phone2 = Phone()
phone2.note = '我是phone2的专有属性note'

print('phone1 call is addr :', id(phone1.call))
print('phone1 call is addr :', id(phone2.call))

phone1.type = '8'
print(Phone.type, phone1.type, phone2.type)
# init执行时机
'''
    1、加载类到内存
    2、p = Phone() 做了几个动作。第一步找有没有空间Phone. 第二步 向内存申请和Phone一样的空间。
        第三步，类里有没有__init__魔术方法。如果没有，则执行将开辟的内存给对象名p.
        如果有__init__,则执行里面的动作。此时里面的self就是刚创建的空间。然后赋值给p.
'''

p1 = Person('zbj', 45)
p2 = Person('km', 40)
p1.run()
p2.run()
p1.eat('牛排')
p2.eat('红烧肉')

# 类方法
dog1 = Dog('大黄')
dog1.run()
print('--------->调用类方法')
Dog.test()
Dog.nickname = 'kite'  # 类的属性也可以动态增加
Dog.age = 5  # 类的属性也可以动态增加
print('dog1.age', dog1.age)
dog1.run()
dog1.test()  # 对象也可以调用类的方法。
Dog.run(dog1)  # 类也可以调用对象的方法。太随意了。真是。
Dog.test1()
dog1.test1()

#静态方法
print('---------->静态方法')
Person.test()