strtemp = '2018 Amazon Jeff Bezos 1120'

#1去掉2018+空格
str1 = strtemp[5:]
print(str1)

#2得到纯数字
str2 = ''.join([x  for x in strtemp if x.isdigit() ])
print(str2)