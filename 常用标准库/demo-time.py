'''
1 time.time() 时间戳 执行代码时间差。
2 time.ctime()
3 time.localtime()
4 time.mktime() 元组转时间戳
'''
import time
t = time.time()
print(t)
count = 0
for i in range(100000):
    count += i


t1 = time.time()
print(t1-t)

print(time.ctime(time.time()))
print(time.localtime(time.time()))