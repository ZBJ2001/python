'''
正则表达式
^
&

'''
import re

#用户名可以是字母或数字_,不能是数字开头，用户长度大于5.
username = 'admin001'
result = re.match('[a-zA-Z][0-9a-zA-Z]{5,}$',username)

result = re.match('[a-zA-Z]\w{5,}$',username)
print(result)


#匹配字符串是否以“mr_"开头，不区分字母大小写
pattern = r'mr_\w+' #模式字符串
str1 = 'MR_SHOP mr_shop'
match = re.match(pattern,str1,re.I)
print('匹配值的起始位置:',match.start())
print('匹配值的结束位置:',match.end())
print('匹配位置的元组:',match.span())
print('要匹配的字符串',match.string)
print('匹配数据:',match.group())
print(match)
str2 = '项目名称MR_SHOP mr_shop'
match = re.match(pattern,str2,re.I)
print(match)


match = re.search(pattern,str1,re.I)
print(match)

match = re.search(pattern,str2,re.I)
print(match)

match = re.findall(pattern,str1,re.I)
print(match)

match = re.findall(pattern,str2,re.I)
print(match)


pattern = r'[1-9]{1,3}(\.[0-9]{1,3}){3}' #模式字符串
str1 = '127.0.0.1 192.168.1.66'
match = re.findall(pattern,str1)
print(match)

pattern = r'([1-9]{1,3}(\.[0-9]{1,3}){3})'
match = re.findall(pattern,str1)
print(match)


