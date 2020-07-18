'''
列表 list 容器
1、创建列表
    列表的特点
        没有长度限制
        可以存放任意类型
        允许存放重复元素。
2、访问内容
    同字串下标。
    变量[下标]
    下标从0开始。len(列表)返回列表的长度。 用长度-1，因为从0开始。
    切片 变量[:]

3、内置集数
    增加
        append():列表的末属追加
        extend():把两个列表合并 该方法没有返回值，但会在已存在的列表中添加新的列表内容。
        insert():插队
    删除
        remove():移动列表中第一个符合名称的值。如果找不到会报错。需要加异常处理
        pop()  pop([index]) 删除下标位置，如果不传位置，删除最后一个。 如何传递下标超出范围如何处理。
        clear() 清空内容，地址保留。
        del 列表[下标] 可以使用切片
        del 列表
    改:
        numbers[1] = 9 修改


    查:
        numbers.index(6) 查找对象对应的位置。如果没有报错。返回位置序号
        list.index(x[, start[, end]]) 理论上还是包前不包后
    其他函数：
        补充：
        join() 合并。结合列表使用。 合并时，列表中的元素必须是字符。将列表合并成字符串
            Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
            str = "-";
            seq = ("a", "b", "c"); # 字符串序列
            a-b-c
        copy()
        count(元素) 某个元素出现的次数
        lists = [[1, 2, 3], [1, 3, 4, 5], [3, 5, 5, 6], []] #列表。
        print(lists[0][0]) #调用列表里的列表。
        count()： list.count(需要查找值) 统计有多少个要查找的值。
        sort():
            描述
            sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
            语法
            sort()方法语法：
            list.sort(cmp=None, key=None, reverse=False)
            参数
            cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
            key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
            reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
            返回值
            该方法没有返回值，但是会对列表的对象进行排序。

        排序的三种方式
            1、sorted（list1,reverse = True) 降序
            2、list1.sort(reverse = True) 对列表直接排序
            3、list1.sort() 升序排列，list1.reverse() 返转

        reverse():

        cmp(list1,list2)比较列表的元素是不是一样 新版本不能用。 用-或其他 方法
4、列表支持的符号
    + list1 +list2 相当于append.
    * list*2
    []下标
    [:]切片
    in 元素在不在列表中。
    is 地址的比较
    for 遍历列表。

5、 len() 返回列表,字符串,元组的长度.
    min()最小值
    max()最大值
    sum()

6、常用函数
    isinstance 判断类型
    type

    isinstance() 与 type() 区别：
    type() 不会认为子类是一种父类类型，不考虑继承关系。
    isinstance() 会认为子类是一种父类类型，考虑继承关系。
    如果要判断两个类型是否相同推荐使用 isinstance()。
    isinstance(B(), int)    # returns True
    type(B()) == int        # returns False
'''
import random


# 列表的新建，增删改查 切片
def fun1():
    cars = []  # 空列表 创建
    cars = ['车0', '车1', '车2', '车3', '车4']  # 定义有内容的列表。
    scores = [99, 89, 100, 70, 51, '0分']
    # 以下为切片
    print(cars[len(cars) - 1])  # 列表最后一个元素。长度减1.因为是从0开始。

    print(cars[-1])  # 列表最后一个元素，切片同字符串
    print(cars[::-1])  # 逆序输出
    print(cars[1:4:2])
    print(cars[-2::-2])

    # 增加元素
    cars.append('增加车5')
    cars.insert(1, '插队1')  # 插队到1位置，其他位置后移。
    cars.append('增加车6')
    cars.insert(len(cars) - 1, '插队车2')  # 插队插不到最后一个位置上，最后插到倒数第二的位置上。

    # 删除元素
    del cars[0]
    cars.pop()  # 删除最后一个
    cars.pop(0)  # 删除和一个
    # cars.pop(50) #报错 IndexError: pop index out of range
    cars.remove('插队车2')
    # cars.remove('无此车') #ValueError: list.remove(x): x not in list

    if '插队车51' in cars:  # 查不到不报错
        cars.remove('插队车51')

    try:
        i = cars.index('车33')  # 查不到会报错
    except:
        print('查无此车')

    try:
        i = scores.index(89, 0, 1)  # 查不到，因为从0开始，到1结束，但不包括1.
    except ValueError:
        print('{0}查不到89，因为从0开始，到1结束，但不包括1.'.format(scores))
    except Exception:
        print('其他错误的出现')
    else:
        print('无错误的情况')

    print('----------------->')
    print(cars)
    print(scores)
    print(cars.extend(scores))  # 该方法没有返回值，但会在已存在的列表中添加新的列表内容。
    print(cars)


# 列表的其他函数
def fun2():
    nums = [1, 6, 3, 4, 5]
    # join
    str1 = 'zbj'  # 合并的分隔符
    print(str1.join(['1', '2', '3']))
    # print(str1.join(nums))
    # copy练习
    numscopy = nums.copy()  # 生成一个新列表。值相同。不是引用关系 。
    nums[4] = 4
    print(numscopy)

    # 系统几个用于列表的函数练习
    print('{0}列表的长度是{1}'.format(nums, len(nums)))
    print('{0}列表的最大值是{1}'.format(nums, max(nums)))
    print('{0}列表的最小值是{1}'.format(nums, min(nums)))
    print('{0}列表的和是{1}'.format(nums, sum(nums)))

    # 列表的方法
    print('{0}列表的4现出{1}'.format(nums, nums.count(4)))
    print('{0}列表返转为{1}'.format(nums, nums.reverse()))  # 这个很有意思，Nums已返转，返回值是None

    print('{0}列表排序为{1}'.format(nums, nums.sort()))  # 这个很有意思，Nums已排序，返回值是None
    print('{0}列表排序为{1}'.format(nums, nums.sort(reverse=True)))  # 这个很有意思，Nums已排序，返回值是None

    print('isinstance(car, list)值是', isinstance(nums, list))

    # print('isinstance(car, list)值是',isinstance(nums, good)) 无效的类型会报错
    print(type(nums))
    if type(nums) == list:
        print('类别是list')


# 列表操作符练习
def fun3():
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2 = list1.copy()
    print('list1 address:', id(list1))
    print('list2 address:', id(list2))
    lists = [[1, 2, 3], [1, 3, 4, 5], [3, 5, 5, 6], []]  # 列表。
    print(lists[0][2])  # 调用列表里的列表。
    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 6, 7, 8]
    list1 = list1 + list2
    print(list1)
    print(list1 * 2)

    # for car in cars:
    #     print(car)


fun2()
exit()

# 问题 列表中0元素删除后，当前的索引位置变吗？
# list1 = [0, 1, 2, 3, 4, 5]
# for i in list1:

