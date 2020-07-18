import math
# print(dir(math))
# for i in dir(math):
#     print(i)
#控制方向 正向逆向 切片
'''
    字符串
    内置字符串方案
    find,rfind,index,rindex
    字符串切片练习
    str = 0123456789
    str[0:0] = '' 空字符串
    str[0:1] = '0'
    str[:10] = '0123456789'
    str[-1:-2:-1] = '9'
    
'''


str = '0123456789'
print(str[0:0])

print(str[-3:-6:-1])
print(str[3::-1])


ss='https://tieba.baidu.com/f?kw=white&ie=utf-8&tab=album'

index = ss.find('/') #查不到返回-1
print(index)
print(ss[:index]) #这个是首先找到位置，截到找到之前的。
index = ss.rfind('/')#倒着找
print(ss[index+1:])

index = ss.find('/') #查不到返回-1
index = ss.find('/',index,5 )
#找到第三个/如何做
ss='https://tieba.baidu.com/f?kw=white&ie=utf-8&tab=album/hello.jpg'
index = 0
for i in range(0,3):
   # print('bool(i):',bool(i)+0)
    index = ss.find('/',index+bool(i)) #i=0,加零，i大于0，全都 加1.利用bool特性。当然也可以用if.
    if index == -1: break

print('index :%d'%index)
print(ss[:index])

start = ss.find('=')
end = ss.find('&')

print(ss[start+1:end])
index = ss.rfind('/')  #从右而查 索引也是从左侧计数。
print(ss[53+1:])
#ss.index() #查不到报错
