'''
递归函数
    1、函数自身调自身。
    2、一层层的进入函数，一层层的退出函数，然后执行函数后面的代码。1，2，3的进入，3，2，1的退出。
    3、有一个入口
    4、设定一个终点。
'''


#1到100的累加和。
def sum(n):#1到n

    if n==0:
        return 0
    else:
        return n+sum(n-1)
print(sum(10))


def f1(n):
    if n>0:
        print('---->',n)
        f1(n-1)
        print('-----{}结束'.format(n))
    else:
        print('-------结束！')

f1(3)