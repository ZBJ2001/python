'''
列表推导式
    #格式：[表达式 for 变量 in 旧列表]
        [表达式 for 变量 in 旧列表 if 条件]
字典推导式
集合推导式
'''
import random

# 使用列表推导式可以快速生成一个列表，或根据某个列表生成满足指定需求的列表。
# 1 生成指定范围的数值列表
randomnumber = [random.randint(10, 100) for i in range(10)]
print(randomnumber)

# 根据列表生成指定需求的列表
prices = [1200, 5330, 2988, 6200, 1998, 8888]
sales = [int(x*0.5) for x in prices]
print(sales)
print([int(x*0.5) if x > 300 else int(x*1) for x in [100,200,300,400,50] if x > 100])

exit()
#从列表中选择和符合条件的元素组成新列表
sales = [x for x in prices if x > 5000]
print("原列表：",prices)
print('价格高于5000的：',sales)


names = ['tom', 'lily', 'abc', 'zbj', 'km', 'jack', 'karray']
# 过滤掉长度小于3的元素 类似filter()
print(list(filter(lambda x: len(x) > 3, names)))

# 推导式
list1 = [name for name in names if len(name) > 3]  # 第一个name是导出的新元素
print(list1)



# 过滤后首字母变大写
list1 = [name.title() for name in names if len(name) > 3]
print(list1)

# 1-100之间能被三整除的组成新列表
print([i for i in range(1, 101) if i % 3 == 0])

# 1-100之间能被三又能被5整除的组成新列表
print([i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0])


# 0-5偶数和0-6的奇数。组成元组列表[(0,1),(0,3),(0,5),(2,1)...]
def func():
    newlist = []
    for i in range(5):  # 偶数
        if (i % 2 == 0):
            for j in range(10):
                if (j % 2 != 0):
                    newlist.append((i, j))
    print(newlist)


func()

# 第一个for是外层循环，第二个for是内层循环
print([(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0])

# 元素是列表，取其最后一个元素。即取元素的最后一个元素。
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]]
print([x[2] for x in list1])
print([x[-1] for x in list1])

# if 工资大于5000，加200.如果低于等于5000，加500
dict1 = {'name': 'tom', 'salary': 5000}
dict2 = {'name': 'luck', 'salary': 4500}
dict3 = {'name': 'jack', 'salary': 3000}
dict4 = {'name': 'jack', 'salary': 8000}

list1 = [dict1, dict2, dict3, dict4]
# 前面是大于5000，后面是小于5000
print([person['salary'] + 200 if person['salary'] > 5000 else person['salary'] + 500 for person in list1 if person['salary']>2000])

print([person['salary'] + 200 if person['salary'] > 5000 else person['salary'] + 500 for person in list1])
