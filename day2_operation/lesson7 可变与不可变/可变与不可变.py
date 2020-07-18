'''
值改变了，地址发生改变了，就是不可变类型
int,str,float,tuple

地址不改变，就是可变类型。就是值可以改变。
list,set,dict

类型转换
str()
int()
list()
dict()
set()
tuple()
str-> int,list,set,tuple
'''

n = 10
print(id(n))
n = 11
print(id(n))

s = 'hello'
print(id(s))
s = 'hello1'
print(id(s))

list1 = [1,2,3,4,5]
print('list1 addr:',id(list1))
print('list1 addr[0]:',id(list1[0]))
list1[0] = 2
print('list1 addr:',id(list1))
print('list1 addr[0]:',id(list1[0]))

exit()

tuple1 = ()

print(type(tuple1))
dict1 = {}
print(type(dict1))
set1 = set()
print(type(set1))
list1 = []
print(type(list1))

print((1,)+(2,))
d = {}
d['a'] =3
print(d)
print(list(d.items()))
*a,b,c = 1,2,3,4,5,6

print(a,b,c)
*a,b = (1,2,3,4)
print(a)
