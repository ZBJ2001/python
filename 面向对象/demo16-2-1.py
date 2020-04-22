'''
继承
    super() 表示父类对象
特点：
    1、如果类中不定义__init__，调用父类的。如果自己有，调用自己的。
    2、父类有eat,子类也有eat.搜索原则是和无找当前类。然后再找父类。这个型为叫重写。override.覆盖
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):

        print('{}正在吃东小馆... 父类方法'.format(self.name))

    def run(self):
        pass

class Student(Person):
    def __init__(self,name,age,clazz):
        super().__init__(name,age)
        self.clazz=clazz
    def study(self):
        print('{}正在学习....'.format(self.name))

    #子类有与父类同名方法
    def eat(self,food):
        super().eat()
        print(self.name+'正在吃'+food+'....子类同名方法调用。')

class Employee(Person):
    def __init__(self,name,age,salary,manager):
        print('Emplyee __init__')
        super().__init__(name,age)
        self.salary = salary
        self.manager = manager

class Doctor(Person):
    def __init__(self,name,age,patients):
        super(Doctor, self).__init__(name,age)
        self.patients = patients

    def show_patients(self):
        print(self.patients)

s = Student('zbj',45,'机电工程计算机应用95-1')
s.eat('锅包肉')
s.study()

e = Employee('km',41,5500,'lzp')
e.eat()

patients = ['z3','l4','w5']
d = Doctor('doctor',50,patients)
d.show_patients()