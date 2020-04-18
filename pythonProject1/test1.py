from pip._vendor.distlib.compat import raw_input

print ("hello world!");
print ("第二行"); print ("第三行！");

'''
这是多行注释，使用单引号。
大段的注意用这个来实现
'''

"""
这是多行注释 ，使用双引号。
功能同上。
"""

#这是单行注释 。
raw_input("按下 enter 键退出，其他任意键显示...\n");

x="a";
y="b";
#换行输出
print (x);
print (y);
# 不换行输出 不对。
print (x);
print (y),;
print (x,y);


i=1
while i<10:
    j=1
    while j<=i:
        print("%s*%s=%s"%(j,i,i*j),end=" ")
        j+=1
    print("\n")
    i+=1