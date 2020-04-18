'''
面向对象
    特征称作属性
    动作称作方法

    先有需求，找出共性，代码上先写类。
    1、所有的类名要求首字母大写，多个单词使用驼峰式命名法
    2、默认继承Object
    3、class 类名[(父类)]:
        属性:特征
        方法:动作
    4、Python可以动态构建类，是python特点。
    5、属性分为：类属性和对象属性
        先找对象属性，如果对象属性没有，则找类的属性。这和以前的面向对象的是不一样的。

    6、方法种类：普通方法，类方法，静态方法，魔术方法（系统自带）。
'''


class Phone:
    # 属性
    brand = '华为'
    # 方法
    def call(self):
        print('self-------->',self)
        print('正在打电话....')
        print('对象的属性note',self.note)

class Student:
    name = 'zbj'
    age = 45


myPhone = Phone()
print(Phone)
print(myPhone)
print(myPhone.brand)
myPhone.brand = '苹果'
print(myPhone.brand)
print(Phone.brand)




#对象动态加专属属性
myPhone.note = 'myPhone自动加的属性'
print(myPhone.note)
phone1 = Phone()
#print(phone1.note) #phone1没有这个属性，同一个类的对象，出现了不同的属性。
myPhone.call()
Phone.call(myPhone)