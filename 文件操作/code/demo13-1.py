'''
异常处理

    try:
        pass
        可能出现异常的代码
    except:
        如果有异常执行的代码。
    finally:
        无论有无异常都执行的代码。
'''


def func1():
    try:
        n1 = int(input('输入第一个数字：'))
        n2 = int(input('输入第二个数字：'))
        oper = input('输入运算符号 + - * /')
        if oper == '+':
            sum = n1 + n2
        elif oper == '-':
            sum = n1 - n2
        elif oper == '*':
            sum = n1 * n2
        elif oper == '/':
            sum = n1 / n2
        else:
            print('符号选择错误！')
            return
        sum = n1 + n2

        print('sum = n1 + n2 ----->', sum)

        # with open(r'e:\p1\aa.txt','wt') as wstream:
        #     wstreawm.write("本次运行的结果是{}".format(sum))

        # with open(r'e:\p1\bb.txt') as rstream:
        #     print(rstream.read())
        list1 = []
        list1.pop()
            #异常匹配是从上向下顺序匹配。
    except ZeroDivisionError:
        print('除数不能为零！')
    except ValueError:
        print('必须输入数字！')
    # except NameError:
    #     pass
    # except FileNotFoundError:
    #     pass
    except Exception as err:
        print('出错了！',err)

    #如果是多个except，最大的放在最后。


def func2():
    try:
        n1 = int(input('输入数字：'))
        print(n1)
        return 1
    except ValueError:
        print('必须是数字...')
        return 2
    else: #只要没报错,就会进入else.但try中有return.是有问题的.永远无法进入到else
        print('数字输入完毕!') #没有异常才会执行的代码块


def func3():
    stream =None #块内声明变量其他块无法直接访问.所以先声明一下
    try:
        stream = open('e:/p1/aa.txt')
        container = stream.read()
        print(container)
        return 1
    except Exception as err:
        print(err)
        return 2
    finally:
        print('---------finally------------')
        if stream:
            stream.close()
        return 3
    #如果有finally，一定会执行finally。

#抛出异常
def func4():
    username = input('输入用户名：')
    if len(username)<6:
        raise Exception('用户名长度必须6位以上')
    else:
        print('输入用户名{0}'.format(username))

func4()
