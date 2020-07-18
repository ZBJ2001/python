'''
字典
    字典使用场景
    字典特点
    1、键值对保存
    2、键不能重复，但是值是可以重复的
    3、字典没有下标和索引，底层实现也是哈希表
    字典声明
        空字典：
            dict1 = dict() #声明一个空字典
            dict2 = {} #声明一个空字典
        有内容的字典：
            dict3 = {'z3':{'活着','红楼梦'}，'李四':{'活着','平凡的世界'}}
    字典元素获取
        dict3[key] 根据key得到value 如果没有指定的key.报错keyError
        dict1.get[key[,default]) --->value 这个不报错
    字典的内置函数
        get() 常用方法。
        value = dict1.get(key)  如果找不到，返回None
        value = dict1.get(key,1)  如果找不到，返回1,默认值

    字典支持的符号
        in
        for key,value in dict3.items():
         print(key,value)

        for e in dict3:
        print(e)#只能打出KEY

        if key in dict1: 检查KEY是不是包含。

    字典的增册改查
    填加：dict[key]=value
    修改：dict[key]=value 修改和填加一样。如果有key，则修改，如果无就是填加。
    删除：dict.pop(key) 根据key删除，返回key的值。
            描述
            Python 字典 pop() 方法删除字典给定键 key 及对应的值，返回值为被删除的值。key 值必须给出。 否则，返回 default 值。
            pop()方法语法：pop(key[,default])
            参数
                key: 要删除的键值
                default: 如果没有 key，返回 default 值
            返回值
                返回被删除的值。
          dict.popitem()随机删除 返回元组。
            描述 Python 字典 popitem() 方法返回并删除字典中的最后一对键和值。
            如果字典已经为空，却调用了此方法，就报出 KeyError 异常。
            语法
                popitem()方法语法：
                popitem()
            参数
                无
            返回值
                返回一个键值对(key,value)形式。

          dict.clear()
          del dict1[key] 根据key删除键值对。类似pop
          del dict1 清空内容并回收内存
    查找：
        没有。
        但是我们可以取值。
        取值：keys(),values(),items()

    列表转字典： 符合一定格式的可以。[(a,b),(c,d)]这种可以。
    字典转列表：这个随意转，只转出来KEY


list []--->[1,3,5]
tuple()--->(1,3,5)
set{}--->{1,3,5}
dict() key:value
'''


# 字典新建，增删改查
def func1():
    dict1 = dict()  # 声明一个空字典
    dict2 = {}  # 声明一个空字典
    print(type(dict2))

    dict3 = {'张三': 20, '李四': 30, '王五': 19}
    dict4 = {'张宝军': 45, '张潇': 17, '张宇瑞': 8}
    value = dict3.get('赵')  # 返回None
    value = dict3.get('赵', 18)  # 返回None
    print("dict4.get('张宝军')", dict4.get('张宝军',21))
    print("dict4.get('张宝')", dict4.get('张宝',21))
    print("dict4['张宝军']",dict4['张宝军'])
    dict4['张慈明'] = 71  # 没有KEY，是填加
    dict4['张宝军'] = 44  # 已有KEY,则修改。
    print(dict4)
    print(str(dict4))

    print("dict4.pop('张宝军') 返回值是：",dict4.pop('张宝军'))# 根据key删除，返回key的值。

    print("dict4.popitem('') 返回值是：",dict4.popitem())# 删除最后一对键和值 返回的是元组类型
    value = dict4.popitem()


    print(type(value))
    print(dict4)
    result = dict.fromkeys(['a', 'b', 'c'], 100)  # 构建一个新的字典。通过iterable
    print(result)
    for i in result: #这里默认是迭代key
        print(i)
    for key in result.keys():
        print(key)
    for value in result.values():
        print(value)
    for key,value in result.items():
        print(key,value)


    list1 = [(1, 2), (3, 4)]

    dict2 = dict(list1)
    print(dict2)

func1()
exit()

#
# result = dict3.keys()  # 把字典里的KEY全取出来 返回类型dict_keys。可以强转为列表
# result = list(dict3.values())
#

