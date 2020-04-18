'''
^
&

'''
import re

#用户名可以是字母或数字_,不能是数字开头，用户长度大于5.
username = 'admin001'
result = re.match('[a-zA-Z][0-9a-zA-Z]{5,}$',username)

result = re.match('[a-zA-Z]\w{5,}$',username)
print(result)