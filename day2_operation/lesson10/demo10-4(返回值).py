'''
返回值，是函数向外送值的。
参数是外部向函数内部送值的。

return 没有值或没有return 函数返回None
return 可以返回多个值。先装包为元组，然后返回 python独有。
'''

list1 = [3, 5, 8, 9, 9, 3]

#找到最大值
def find_max(list1):
    if isinstance(list1,list): #判断变量是不是list类型
        max = list1[0]
        for i in list1:
            if i>max:
                max = i
        return max,i #返回值，结束函数调用。 同时返回两个值。返回的是一个元组

a = find_max(list1)
print(*a)


def find_max2(list1):
    if isinstance(list1,list):
        max1 = list1[0]
        max_index = 0
        for index,i in enumerate(list1): # 和迭代字典一样了。
            if i > max1:
                max1 = i
                max_index = index
        return max1,max_index #先装包，封装为元组返回。