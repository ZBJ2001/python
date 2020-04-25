'''
模块是代码组织的一种方式，把功能相近的函数或类放在一个文件中，一个文件（.py)
模块名就是文件名去掉后缀py.


导入模块
1 import 模块名 调用时用  模块名.
2 from 模块名 import 变量/函数/类
3 from 模块名 import * 引入该模块中所有的内容。如果需要限制。__all__ = ['','','','']

4  无论from 还是import　 模块在导入时会加载所有的内容和执行。
    如果不希望调用，就会用到__name__

'''
import random #导入模块 这样调用是 模块.成员。
import calculate
from calculate import add
from calculate import number,name,Calculater







# for i in range(1,10):
#     r = random.randint(1, 10)
#     print(r)

#调用模块里的函数 模块名.变量/函数/类。
list1 = [2,3,4,5]
print(calculate.add(*(list1)))

print('calculate.number',calculate.number)
calculate.Calculater(10).test()
calculate.Calculater.test1()
calculate.Calculater.test2()

print(add(1,3,43,number))
print(name)

Calculater(10).test()