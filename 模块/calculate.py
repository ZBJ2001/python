
#列表里的是import * 导入的成员
__all__ = ['']
# 变量
number = 100
name = 'zbj'


# 函数
def add(*args):
    print(args)
    if len(args) > 1:
        sum = 0
        for i in args:
            print(i)
            sum += i

        return sum
    else:
        print('至少传入两个参数！')
        return None  # 默认


def minus(*args):
    if len(args) > 1:
        minu = 0
        for i in args:
            minu -= i
        return minu
    else:
        print('至少传入两个参数！')
        return 0


def multiply(*args):
    pass


def divide(*args):
    pass


# 类
class Calculater:

    def __init__(self, num):
        self.num = num

    def test(self):
        print('正在使用Calculate进行运算...')

    @classmethod
    def test1(cls):
        print('-------->Calculater中的类方法')

    @staticmethod
    def test2():
        print('-------->Calculater中的静态方法')




def test():
    print('--------->测试代码 ')
print('__name__:',__name__)
if __name__ == '__main__':
    print('__name__:',__name__)
    test()