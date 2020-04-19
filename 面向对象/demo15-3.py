'''
魔术方法
1.__init__  重点
初始化魔术方法
    触发时机：初始化对象时触发（不是实例化触发，但是和实例化在一个操作中）
    参数：至少有一个self，接收对象
    返回值：无
    作用：初始化对象的成员
    注意：使用该方式初始化的成员都是直接写入对象当中，类中无法具有
2.__new__
实例化魔术方法
    触发时机： 在实例化对时触发
    参数：至少一个cls 接收当前类
    返回值：必须返回一个对象实例
    作用：实例化对象
    注意：实例化对象是Object类底层实现，其他类继承了Object的__new__才能够实现实例化对象。
    没事别碰这个魔术方法，先触发__new__才会触发__init__

3.__del__
析构魔术方法
    触发时机：当对象没有用（没有任何变量引用）的时候被触发
    参数：一个self 结婚搜对象
    返回值：无
    作用：使用完对象是回收资源
    注意：del不一定会触发当前方法，只有当前对象没有任何变量接收时才会触发
4.__call__
调用对象的魔术方法
    触发时机:将对象当作函数调用时触发 对象()
    参数:至少一个self接收对象，其余根据调用时参数决定
    返回值：根据情况而定
    作用：可以将复杂的步骤进行合并操作，减少调用的步骤，方便使用
    注意：无
5.__len__
    触发时机：使用len(对象) 的时候触发
    参数：一个参数self
    返回值：必须是一个整型
    作用：可以设置为检测对象成员个数，但是也可以进行其他任意操作
    注意：返回值必须必须是整数，否则语法报错，另外该要求是格式要求


6.__str__  重点
    触发时机:使用print(对象)或者str(对象)的时候触发
    参数：一个self接收对象
    返回值：必须是字符串类型
    作用：print（对象时）进行操作，得到字符串，通常用于快捷操作
    注意：无

7.__repr__
    触发时机:在使用repr(对象)的时候触发
    参数：一个self接收对象
    返回值：必须是字符串
    作用：将对象转使用repr化为字符串时使用，也可以用于快捷操作

8.__bool__
    触发时机: 使用bool(对象)的时候触发
    参数：一个self接收对象
    返回值：必须是布尔值
    作用：根据实际情况决定，可以作为快捷方式使用
    注意:仅适合于返回布尔值的操作

9.__format__
    触发时机：使用字符串.format(对象)时候触发
    参数：一个self接收对象，一个参数接收format的{}中的格式，例如:>5
    返回值:必须是字符串
    作用：设置对象可以作为format的参数，并且自定义对象格式化的规则
    注意：无



  sys.getrefcount(p) #关于地址的引用次数。

'''
import sys


class Person:
    def __init__(self,name):
        print('-------->init')
        self.name = name

    def __new__(cls, *args, **kwargs):
        print('--------->new')
        position = object.__new__(cls) #这个地址就是返回给对象的地址。
        return position

    #将对象当函数调用时触发。
    def __call__(self, *args, **kwargs):
        print('------------->call')
        print(args)


    def __del__(self):
        print('----------->del')

    def __str__(self):
        return '姓名是:'+self.name

    def func(self):
        print('普通方法')

    @classmethod
    def classfunc(cls):
        print('类方法，通过类名调用，也可以对象调用')

    @staticmethod
    def staticfunc():
        print('静态方法')
p = Person('zbj')
#对象当函数使用方式
p()
p('hello')
p('zbj','km')
p1 = p
p2 = p
print('id(p1)',id(p1))
print('id(p2)',id(p2))

del p1
del p2
print('sys.getrefcount(p)',sys.getrefcount(p))

# __str__魔术方法的使用
#没用时 显示的是对象的地址。
print(p)
print(str(p))

