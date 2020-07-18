import random  # 引用随机数的库

# 语句
'''
1、条件语句 主要是看缩近
    if 条件：（结果是布尔类型的 关系运算符，逻辑运算符，成员，身份，布尔）
        条件成立执行的代码
    else:
        不成立执行的代码

2、嵌套使用
    if 条件：
        if 条件：
        else:
    else:
        if 条件：
        else:

3、多重条件判断
    if 条件：
    elif:
    elif:
    else:


4、pass:不做任何事情，只起到占位的作用

5、格式化字符串
    '字串%要' %变量
    %s:字符串占位符
    %d 专门给整型占位。即使给的不是整型，也会强制转换成整型。如果给的是字符串，会报错
    %f 给浮点型占位。%.1f 保留一位小数。%.3f 保留3位小数。
    格式化字串新方法format 以上方法不常用。

 6、random.randint(0, 9) 取得0-9之间的随机整数
    Return random integer in range [a, b], including both end points. 
    返回随机整数，包括两个端点
    random.random() 产生随机小数
    randrange() 方法返回指定递增基数集合中的一个随机数，基数默认值为1。
    round()小数的四舍五入
    
 7、break 退出当前循环。
    continue 忽略后面代码，继续执行循环。
'''


# 判断年龄 练习if,占位符
def fun1():
    age = input('输入你的年龄：')
    age = int(age)
    if age > 18:
        print("您已成年")
        game = input('输入游戏名字：')
        if game == '连连看':
            print('回家玩吧！')
        else:
            print("我喜欢玩：%s" % game)  # 字符串格式的方式。
    else:
        print("您还未成年")
        print("不要乱跑")

    print('%s喜欢玩%s,玩了%d年' % ("zbj", "魔兽", 10))


# 停车厂 练习while,list,if..elif
def fun2():
    car_location = []  # 停车场
    while True:
        choice = int(input('请选择功能：1.进场 2.出场 3。查询 4.统计 5.退出'))

        if choice == 1:
            car_in = input('输入车牌号：')
            print(car_in + '进场了')
            car_location.append((car_in))
        elif choice == 2:
            car_out = input('输入车牌号：')
            print(car_out + '出场了')
            car_location.remove(car_out)
        elif choice == 3:
            car_inquire = input('输入车牌号：')
            if car_inquire in car_location:
                print('车辆在场')
            else:
                print('车辆不在场')

        elif choice == 4:
            print('停车场使用数量%d' % len(car_location))
        elif choice == 5:
            print('退出系统')
            break


# 练习break和continue
def fun3():
    i = 0
    while True:
        if i > 10:
            break
        j = 0
        while True:
            if j > 5:
                break
            print(j)
            j += 1

            if j > 3:
                continue
                print('这个代码也不会执行')
            print('continue可以跳过这段代码继续循环。')


        print('----->',i)
        i += 1

#练习占位符 和随机数
def fun4():
    i = random.randint(0,9)
    a = random.randrange(1,10,3)
    money = random.random()
    sale = money * 1000
    round(sale) #小数的四舍五入
    print('随机产生的0-9的整数是%d，随机产生的小数是%.2f,随机产生的小数保留5位小数%.5f'%(i,money,sale))
    print('随机产生的小数以整数形式显示%d，四舍五入值是%d'%(sale,round(sale)))
    print('返回1-10，递增基数是3的随机数是{}'.format(a))



#练习字符串格式化.format
def fun5():
    list = ['jack',18]
    #位置参数
    print('my name is {},age {}'.format('jack',18))
    print('my name is {1},age {0}'.format(10,'jack'))
    print('my name is {1},age {0} {1}'.format(10,'jack'))
    print('my name is {},age {}'.format(*list)) #拆包 成jack,18 **拆成a=1,b=2
    print('my name is {1},age {0}'.format(*list)) #拆包 成jack,18 **拆成a=1,b=2

    #关键字参数
    dict1 = {'name':'jack','age':18}
    print('my name is {name}, age is {age}'.format(name='jack',age=18))
    print('my name is {name}, age is {age}'.format(**dict1))

    #填充与格式化 :[填充字符][对齐方式 <^>][宽度] 冒号前面可以省略。
    print('{name:>10}'.format(name='zbj')) ##右对齐
    print('{1:*<10}'.format(10,20)) ##左对齐
    print('{:*^10}'.format(10)) ##居中对齐

    #精度与进制 #{:.0f}不带小数。
    print('{0:.2f}'.format(1/3))
    print('{0:.5f}'.format(1/3))
    print('{0:b}'.format(10)) #二进制
    print('{0:o}'.format(10)) #八进制
    print('{0:x}'.format(10)) #十六进制
    print('{0:,}'.format(1123412351230)) #千分位格式化

    #使用索引 ？？
    print('name is {0[0]} age is {0[1]}'.format(list))
    print('name is {0[0]} age is {0[1]}'.format(list))



fun5()