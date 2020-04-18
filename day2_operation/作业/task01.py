'''
2.求1--100之间可以被7整除的数的个数

3.计算从1到100以内所有3的倍数的和
'''

def fun1():
    '''
    求1--100之间可以被7整除的数的个数
    :return:
    '''
    count = 0
    nums = []
    for i in range(1,101):
        if (i%7==0):
            count+=1
            nums.append(i)
    print('1--100之间可以被7整除的数的个数{0},分别是{1}'.format(count,nums))

def fun2():
    '''
    计算从1到100以内所有3的倍数的和
    :return:
    '''
    sum = 0
    for i in range(1,101):
        if (i%3 == 0):
            sum += i

    print('从1到100以内所有3的倍数的和{}'.format(sum))

fun2()
