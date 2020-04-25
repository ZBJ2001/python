'''
单例模式

'''
class Singleton:
    #私有化
    __instance = None

    #重写父类的__new__
    def __new__(cls):
        print('--------__new__')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            return cls.__instance



s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)