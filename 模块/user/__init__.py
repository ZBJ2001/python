#只要导包，就会执行这个文件。
'''
1、当导入包的时候，把一些初始化的函数，变量，类定义在__init__.py文件中
2、此文件中函数，变量等访问，只通过包名，函数。
'''
__all__ = ['models']
print('---------------->user.__init__.py')


def create_app():
    print('-----------> create app')

def printA():
    print('----------->AAAAAAAAAAAAA')