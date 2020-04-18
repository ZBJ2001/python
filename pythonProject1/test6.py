#!/usr/bin/python
# -*- coding: UTF-8 -*-

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print (counter);
print (miles);
print (name);

#允许同时为多个变量赋值。
a=b=c=1;

#多个变量分别赋值
a,b,c = 1,2,"zbj";
print (a,b,c);

#以下是字符串操作

str = 'Hello World!'

print (str)  # 输出完整字符串
print (str[0])  # 输出字符串中的第一个字符
print (str[2:5])  # 输出字符串中第三个至第六个之间的字符串
print (str[2:])  # 输出从第三个字符开始的字符串
print (str * 2)  # 输出字符串两次
print (str + "TEST")  # 输出连接的字符串