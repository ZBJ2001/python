'''
父类，基类

'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        pass

    def run(self):
        print('{} 正在吃东西...'.format(self.name))

class Student(Person):
    pass


class Employee(Person):
    pass

s = Student('zbj',45)
s.eat()


