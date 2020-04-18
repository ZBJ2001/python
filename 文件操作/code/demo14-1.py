'''
列表推导式 字典推导式 集合推导式

'''
#过虑掉长度小于3的元素。
names = ['tom','lily','abc','jack','steven','bob']
result = [name for name in names if len(name)>3] #第一个name是新列表的值
result = [name.title() for name in names if len(name)>3] #第一个name是新列表的值

#将1-100之间能被3整除，组成一个新的列表
newlist = [i for i in range(1,100) if i % 3==0]

newlist = [i for i in range(1,100) if i % 3==0 and i % 5 == 0]

#元组列表 [(),(),()] 第一个for 是外层循环，第二个for是内层循环。
newlist = [(x,y) for x in range(5) if x%2 ==0 for y in range(10) if y % 2 != 0]

list1 = [[1,2,3],[4,5,6],[7,8,9]]
newlist = [i[2] for i in list1 ]


def func1(): #模拟列表推导式
    newlist = []
    for i in range(5):
        if i % 2 == 0:
            for j in range(10):
                if j % 2 != 0:
                    newlist.append((i,j))
    return newlist


# x = func1()
# print(x)
print(newlist)