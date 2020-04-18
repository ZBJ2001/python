# 删除列表中相同的元素

def fun1():
    list1 = [1, 2, 3, 5, 1, 2, 3, 5, 6]
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)

    print(list2)


def fun2():
    list1 = [1, 2, 3, 5, 1, 2, 3, 5, 6]
    list1 = list(set(list1))
    print(list1)


# 这个是不对的。列表remove后，列表索引，元素位置都在改变。网上是从后向前删除。保证前面的位置不变。
def fun3():
    list1 = [1, 2, 3, 5, 1, 2, 3, 1, 4, 5, 6]
    list1.sort()
    print(list1)
    temp = None
    index = 0
    for i in list1:
        print('i的值是{}，list1的长度是：{}'.format(i, len(list1)))
        if i <= len(list1) - 1:
            temp = list1[index + 1]
        if temp == i:
            list1.remove(i)
        index += 1

    print(list1)

    '''
        list.sort();
        print("sorted list:%s" % list)
        length = len(list)
        lastItem = list[length - 1]
        for i in range(length - 2,-1,-1):
                currentItem = list[i]
                if currentItem == lastItem:
                        list.remove(currentItem)
                else:
                        lastItem = currentItem
    '''


# fun3()


x = 3
y = 5
x, y = y, x
print(x, y)

x = ['11', '2', '3']
print(max(x, key=len))
x = [3, 5, 7]
print('x[10:]', x[10:])
x[len(x):] = [1, 2]
print(x)

x = [3,5,7]
x[1:] = [2] #这种代码意义何在

print(x)
# print(1 < 2 < 3)
# print(3 or 5)
# print(0 or 5)
# print(3 and 5)
