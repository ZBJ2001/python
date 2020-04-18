'''
列表推导式
    #格式：[表达式 for 变量 in 旧列表]
        [表达式 for 变量 in 旧列表 if 条件]
字典推导式
集合推导式
'''

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
print([(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0])  # 第一个for是外层循环，第二个for是内层循环

# 元素是列表，取其最后一个元素。即取元素的最后一个元素。
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]]
print([x[2] for x in list1])
print([x[-1] for x in list1])

# if 工资大于5000，加200.如果低于等于5000，加500
dict1 = {'name': 'tom', 'salary': 5000}
dict2 = {'name': 'luck', 'salary': 4500}
dict3 = {'name': 'jack', 'salary': 3000}
dict4 = {'name': 'jack', 'salary': 8000}

list1 = [dict1, dict2, dict3,dict4]
#前面是大于5000，后面是小于5000
print([person['salary']+200 if person['salary'] > 5000  else  person['salary']+500  for person in list1] )

print([person['salary']+200 if person['salary'] > 5000  else  person['salary']+500  for person in list1] )
