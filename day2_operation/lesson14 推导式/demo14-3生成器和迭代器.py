'''
一边循环一边推算元素的方式，就是成生器。
得到生成器的方式
1、通过列表推导式得到一个生成器

'''


#[0,3,6,9,12,15,18,21,....27]
print([x*3 for x in range(20)])

#得到生成器
g = (x*3 for x in range(20) )
print(type(g))

#方式1 通过调用__next__()方式得到元素。 每调一次，产生一个元素。
print(g.__next__())
print(g.__next__())
#方式2 如果调用到没有元素，就会抛出异常。StopIteration
print(next(g))
print(next(g))

while True:
    try:
        e = next(g)
        print(e)
    except:
        print('没有更多的元素可以产生！')
        break


#定义生成器的方式二：借助函数完成
#步骤：1定义一个函数，函数中使用yield关键字
#调用函数，接收调用的结果。
#得到的结果就是生成器。
#借自 next() 或 __next__得到你想要的元素。




def func():
    n = 0
    while True:
        n+=1
        yield n #有这个关键字，就是生成器。 等于return + 暂停

g = func()
print(next(g))


#菲波那切数列