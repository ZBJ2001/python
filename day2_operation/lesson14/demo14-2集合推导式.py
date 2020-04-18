'''
集合推导式
类似列表推导式，只是在列表推导式基础上去重。

字典推导式

'''

# 集合推导式
list1 = [1, 2, 3, 45, 2, 2, 3, 5]
set1 = set(list1)
print(set1)

set1 = {x for x in list1}
print(set1)

set1 = {x + 1 for x in list1 if x > 2}
print(set1)

# 字典推导式  作为了解
dict1 = {'a': 'A', 'b': 'A', 'c': 'C','d':'C'}
newdict = {value:key for key,value in dict1.items()}
