import random


class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


class Car:
    def __init__(self, 品牌, 速度):
        self.品牌 = 品牌
        self.速度 = 速度

    def get_time(self, road):
        ran_time = random.randint(1, 10)
        msg = '{}品牌的车在{}上以{}速度行驶了{}小时'.format(self.品牌, road.name, self.速度, ran_time)
        print(msg)

    def __str__(self):
        return '{}品牌的，速度{}'.format(self.品牌, self.速度)


r = Road('连霍高速', 6000)
car = Car('宝马', 120)
print(car)
car.get_time(r)

############################################################
class Student:  # has a 关系 .
    def __init__(self, 学生名字, 电脑, 书):
        self.学生名字 = 学生名字
        self.电脑 = 电脑
        self.books = []
        self.books.append(书)
    def borrow_book(self,book):
        if book in self.books:
            print('已经借过这本书')

class Book:
    def __init__(self,bname,author,number):
        self.bname =bname
        self.author = author
        self.number = number
    def __str__(self):
        return self.bname+'--------'+self.author+'----------'+str(self.number)


class Computer:
    def __init__(self, 品牌, 型号,颜色):
        self.品牌 = 品牌
        self.型号 = 型号
        self.颜色 = 颜色
    def online(self):
        print('正在使用电脑上网...')
    def __str__(self):
        return self.品牌+'-----'+self.型号+'--------'+self.颜色

comp1 = Computer('mac','mac pro 2018','深灰')
book1 = ('盗墓笔记','南派三叔',10)
print(comp1)