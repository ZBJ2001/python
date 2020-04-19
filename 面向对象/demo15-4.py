# 私有化
'''
好处:
    1,隐藏属性不被外界随意修改
    2,可以通过函数完成.
'''
class Student:
    __age = 18

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__score = 59  # 私有化变量

    def __str__(self):
        return '姓名：{}，年龄：{}，考试分数：{}'.format(self.__name, self.__age, self.__score)

    # 定义公有的set,get方法。
    def set_age(self, age):
        if age>0 and age<= 100:
            self.__age = age
        else:
            print('年龄不在规定的范围内！')

    def get_age(self):
        return self.__age


stu1 = Student('zbj', 45)
stu1.set_age(30)

stu1.set_age(130)
print(stu1)


#显示类的自带的属性
print(dir(Student))
#显示对象的自带属性 将私有的 变成_Student__name显示。
print(dir(stu1))
print(stu1._Student__age)

print(stu1.__dir__())


#突然想到判断是不是中文的问题。这里有个知识点是\u
print(len('zbj'))
print(len('张宝军'))
str1 = 'a'
str2 = '张'
for ch in str2:
    print(ch)
    if '\u4e00' <= str2 <= '\u9ffff':
        print('是中文')
    else:
        print('不是中文')