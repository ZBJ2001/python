'''

集合
    字典的一种，没有重复值
    特点：无序，不重复。第一个放进来的，位置不确定。
    底层原理：哈希表
    声明：
        set1 = set() 空集合
    含有元素的集体
        set2 = {'张宝军','张潇','张宇瑞'}
    场景：
        可以用于保存一些不重复，和顺序没有要求的元素。
    是否支持下标与切片：
        不支持下标和切片。
        insert(index,objectd)
        pop(index)
        index(ojbect)
        del list1[index]
        以上集合都不支持。
    集合中的函数
        添加：
            add() 一个元素填加
            update() 联合两个set,去重。 ---->将一组可迭代的对象。类型列表的是extend
            方法用于修改当前集合，可以添加新的元素或集合到当前集合中，如果添加的元素在集合中已存在，则该元素只会出现一次，重复的会忽略。
        删除：
            remove() 传一个元素值。移除这个元素。
            pop() 删除谁返回谁。随机删除。
            clear()
            discard() 如果集合中没有此元素，则什么都不做。
            discard() 方法用于移除指定的集合元素。
                该方法不同于 remove() 方法，因为 remove() 方法在移除一个不存在的元素时会发生错误，而 discard() 方法不会。
        修改：
            不能修改 一定要改，转成列表再转回来。
        查询：
            不能查询
    符号：
        +，*，[],[:]   不支持
    in 有没有在集合中
    is 地址的比较
    集合运算，
    交集&，intersection
    并集|，difference
    差集- union
    对称差集 ^ 就两边都不一样的。 symmetric_difference
问题：
    1、如何快速去掉列表中重复的元素。
        把列表转换为set即可。
'''
import random


def func1():
    set1 = set()  # 创建一个哈希表 空集合
    set2 = {}  # 默认是字典类型
    set3 = {1, 2, 3, 2, 1}  # 赋值后，自动去重。
    set4 = {1, 5, 8, 9}
    set4.add(3)
    set4.update({20})
    set4.update({10,11,12,5})
    set4.remove(20)
    set4.discard(5) #
    print('随机删除一个元素',set4.pop()) #随机删除一个元素

    print(type(set1), type(set2), type(set3), set3,set4,len(set4))
    print('set3&set4',set3&set4)
    print('set3 | set4', set3 | set4)
    print('set3-set4', set3 - set4)
    print('set3^set4', set3 ^ set4)

    #集合也可迭代
    for i in set4:
        print(i)
    if 3 in set4:
        print('{}中有元素3'.format(set4))

func1()
exit()


# 1、随机产生1-20的不重复的数字10个，保存在集合中
def func2():
    set1 = set()

    while True:
        i = random.randint(1, 20)
        if i not in set1:
            set1.add(i)

            if len(set1) == 10:
                break
    print(set1)


set1 = {1, 2, 3, 9, 7, 3, 4}
# 2、对以上集合升序排列

print('升序排列集合', (sorted(set1, reverse=True)))
# list1 = list(set1)
# list1 = sorted(list1, reverse=True)
# set1 = set(list(set1).sort(reverse=True))

# 3、找出最大值，最小值。

print(max(set1))

set2 = {1, 5, 11, 33, 45, 6}
result = set1 & set2
result = set1.intersection(set2)  # 交集
print(result)

result = set1 - set2
result = set1.difference(set2)  # 将差集. 以符号为主。
print(result)

result = set1 | set2  # 并且
result = set1.union(set2)
reuslt = set1.symmetric_difference(set2)
print(result)
# set1.discard()
