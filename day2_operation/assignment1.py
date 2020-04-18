import random
import os
import time

'''
练习
1、打印1-50之间的数字
2、打印1-100的偶数 5个数字一行
3、打印1-100之间奇数的累加和
4、通过循环得到随机16位的银行卡号 您的卡号是 9790-7634-0430-9536 这个格式

5、跳一跳
6、猜数字 
7、求素数
'''

def my_align(_string, _length, _type='L'):
    """
    中英文混合字符串对齐函数
    my_align(_string, _length[, _type]) -> str
    :param _string:[str]需要对齐的字符串
    :param _length:[int]对齐长度
    :param _type:[str]对齐方式（'L'：默认，左对齐；'R'：右对齐；'C'或其他：居中对齐）
    :return:[str]输出_string的对齐结果
    """
    _str_len = len(_string)  # 原始字符串长度（汉字算1个长度）
    for _char in _string:  # 判断字符串内汉字的数量，有一个汉字增加一个长度
        if u'\u4e00' <= _char <= u'\u9fa5':  # 判断一个字是否为汉字（这句网上也有说是“ <= u'\u9ffff' ”的）
            _str_len += 1
    _space = _length-_str_len  # 计算需要填充的空格数
    if _type == 'L':  # 根据对齐方式分配空格
        _left = 0
        _right = _space
    elif _type == 'R':
        _left = _space
        _right = 0
    else:
        _left = _space//2
        _right = _space-_left
    return ' '*_left + _string + ' '*_right



def printXushu():
    i = 2
    while (i < 100):
        j = 2
        while (j <= (i / j)):
            if not (i % j): break
            j = j + 1
        if (j > i / j): print (i, " 是素数")
        i = i + 1

    print("Good bye!")


def jumpGame():
    '''
    跳一跳游戏
    :return:
    '''
    step = 0  # 步数
    num = 0  # 次数
    while True:
        i = random.randint(0, 10)
        time.sleep(random.random())

        if i == 0:
            print('game over')
            break
        elif i % 5 == 0 or i % 3 == 0 and i != 0:
            step += (i * 2)
            num += 1
            print('步数翻倍，本次跳了%d步，总步数%d ' % (i * 2, step))
        else:
            step += i
            num += 1
            print('本次跳了%d步，总步数%d ' % (i, step))
    print('跳了%d步，跳了%d次' % (step, num))


def caicaile():
    '''
    猜猜乐，一局猜三次，每局开头给3分，猜对加分，猜错扣一分.
    玩一局后回复Y继续下一局，否则退出。
    :return:
    '''
    # 1产生数字
    score = 0  # 计分器
    while True:

        os.system('cls')
        number = 3;  # 第局给3分

        guess_result = random.randint(0, 9)
        for i in range(1, 4):
            inputNum = int(input('系统随机数产生完毕，请猜数数字(0..9)：'))
            if inputNum > guess_result:
                number -= 1
                print('猜大了,再小一点就离成功更近了... 还有%d次机会' % (3 - i))
            elif inputNum < guess_result:
                number -= 1
                print('猜小了,再大一点就离成功更近了...还有%d次机会' % (3 - i))
            else:
                print('您猜对了！太幸运了！')
                score += number
                break
        else:
            print('这一局有点背，没准再来一局就赢了')

        answer = input('本局得分%d,总得分%d是否继续猜猜乐？（y/n):' % (number, score))
        if answer != 'y':
            print('欢迎下次再来~~~')
            break

    print('您总得分:', score)


def fun4():
    cardid = ''
    for i in range(1, 17):
        cardid = cardid + str(random.randint(0, 9))
        if not i % 4 and i < 16:
            cardid = cardid + '-'
    print('您的卡号是', cardid)
    return


def fun3():
    '''
    打印1-100之间奇数的累加和
    :return:
    '''
    count = 0
    for i in range(1, 101):
        if i % 2:
            print(i)
            count += i
    print('打印1-100之间奇数的累加和%d' % count)


def fun2():
    '''
    2、打印1-100的偶数
    :return:
    '''
    for i in range(1, 101):  # range(1,101)从1到100的数字
        if i % 2 == 0:

            if i % 5 == 0:

                print('偶数:%s\t' % i, ' ')
            else:
                print('偶数:%s\t' % i, ' ', end='')

    return


def fun1():
    '''
    1、打印1-50之间的数字
    :return:
    '''
    i = 1
    while (i <= 50):
        print('数字', i)
        i += 1
    return

# print(not 0)
# print(not '')
# print(not None)
# print (not 1)

# for 举例

# list1 = ['zbj','ljp','zx','zyr']
# for name in list1:
#     print(name)
#
# str1 = 'hello,world!'
# for ch in str1:
#     print(ch)
