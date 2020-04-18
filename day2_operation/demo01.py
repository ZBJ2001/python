# 单行注释
print('hello world!')

'''
多行注释
还可以作为字符串。主要用作多行注释。
ctrl+shift+f10 执行当前文件。
ctrl+/ 注释快捷键
ctrl+鼠标左键 函数快速查看
ctrl+alt+l 重新格式代码。
1、变量
    弱类型。  名= 值 具体的类型取决于值。
    判断变量类型 type(变量名)
    *args 可以接受多个参数。不定长参数。不传也可以。
    print(self, *args, sep=' ', end='\n', file=None)
    
    

    
    
2、变量声明
    格式：变量名 = 值
    变量的命名规则：
        A:字母，数字，下划线
        B:不能数字开头
        C:不能使用关键字
        D:区分大小写。
        E:见名知义：尽量使用英文。
            驼峰式命名方式 
                普通变量：showName。
                类：第一个首字母也要大写。
            _命名(推荐)：show_name,print_name
3、变量类型
    str：符号：单引号，双引号，三引号，转义字符 +r结合使用。
    int: 整型 10,5,11038
    float 浮点型  1.9,9.9
    bool 布尔型 True,False
    byte 字节型 b'内容' socket编程。网络传输
    
    list 列表 [value,value]
    tuple 元组 (value,value)
    set 集合 {value,value} 集合底层是字典构成的。
    dict 字典 {key:value,key:value}
    
4、变量与操作符的使用。
    算术运算符 + - * / %(求余）  **几次方 // 整除     
        + 字串连接符。   s1+s2
        * 字串重复次数。 s1*3
        / 除数不能为零。
    赋值运算符
        = += -= *= /= %= 
    关系(比较)运算符 返回值True或False
        == != > < >= <= 
        is:比较的是地址。可以通过id()获取地址。
        ==：比较的是内容，是值 
    逻辑运算符
        and or not  与或非 
        返回值是Ture或False.
    位运算符
        HEX 16进制 DEC 十进制 OCT 八进制 BIN 二进制
        8421
        十进制与二进制转换。
        0000 0010 1*2^1 +0 *2^0 注：2^0 = 1
        -3的二进制 补码表示负数。
        步骤：
        1、求3的二进制码 0000 0011 
        2、求反码        1111 1100
        3、求补码 反码+1 1111 1101
        负数的十进制转二进制。
        
        二进制转十进制
        首先看第一位是符号位。如果是1表示负数。如果是0表示的是正数。
        11110000
        步骤
        1、补码：1111 0000 (-1得反码）
        2、反码：1110 1111 (取反得正数） 
        3、求正数：取反 0001 0000
        已知是负数。值是16.结果是-16
        
        八进制转十进制
        155
        步骤
        1*8^2+5*8^1+5*8^0
        八进制转二进制。一个八进制对应三位二进制
        1   5   5
        001 101 101 = 0 0110 1101
        
        & | ~ 位运算的与或非 》 右移 》左移
    三目运算符:
         if else
        
    成员运算符
        in,not in
        
    身份运算符
        is,  is not 
    运算符优先级
     
'''
print('还是这个用着舒服啊。语言越来越人性了！')
print('2')
# 变量，变量声明

number = 10
print(number)
print(type(number))

number = '10'
print(number)
print(type(number))

print(number, 10, 20, 30)
print(number, 10, 20, 30, sep='#')
print(number, 10, 20, 30, sep='*', end='')
print(number, 10, 20, 30, sep='*')

# 查看关键字
import keyword

print(keyword.kwlist)
# 变量类型
name1 = '孙杨'
name2 = "傅园慧"
message = '''1、孙杨获游泳冠军\\
2、傅园慧表情包！'''
print(type(name1), type(name2), type(message))
print(message)
# 如果里面是双引号，外层用单引号。如果里面是单引号，外层用双引号。
link = ' <link rel="stylesheet" href="chrome-search://local-ntp/animations.css"></link>'
print(link)

'''
预定义的转义字符
\n 换行
\t 制表位，4个空格
\r 
\'
\" 打印引号
\\ 打印斜杠
结合：r'内容’  raw原始的。保留原始样式
'''
s1 = 'hello\nworld'  # \n转义字符
print(s1)
s2 = r'hello\nworld'  # r 保留字符串的原有格式 。

age = 21
print(type(age), age)  # <class 'int'> 判断结果

money = 9999.99
print(type(money), money)  # <class 'float'> 不区分双精度 ，单精度。
flag = True
flag = False  # 真或假首字母必须大写。
print(type(flag), flag)  # <class 'bool'>

b1 = b'hello'  # bytes类型，字节类型。前面b'字串'
print(type(b1), b1)

# 列表类型 list
scores = [98, 89, 91, 100]
print(type(scores), scores)
# 元组 tuple
scores = (1, 3, 2, 4, 5)
print(type(scores), scores)

# 集合 set 集合不允许有重复元素。
scores = {1, 3, 4, 5, 5, 6, 4, 5}
print(type(scores), scores)

# 字典dict key:value
scores = {'张三': 90, '李四': 88, '王五': 99}
print(type(scores), scores)

# 算术运算符
a = 10
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)  # 求余
print(a ** b)  # 10^5
print(a // b)  # 整除

# 赋值运算符
result = a + b
print(result)

# id()内置函数，获取变量地址。返回整型值。
d = 4000
print('b的地址{0},d的地址{1}'.format(id(b), id(d)))

e = 1
e += 6  # e必须先声明 。e = e+6
print(e)

# 关系运算符
print('关系运算符')
a1 = 1000
a2 = 1000
print(a1 < a2)
print(a1 == a2)  # 比较的是内容
print(a1 != a2)
print(a1 is a2)  # is 是比较地址的

# 逻辑运算符
print('逻辑运算符')
a = 0
print(not a)  # true
a = 8
print(not a)  # false
a = ''
print(not a)  # true
a = None # 空值
print(not a)  # true
a = '0'
print(not a)  # false
print(not 3 + 5)
print(5 + True)  # True 运算是1，False 是0
print(5 > True) #关系中True 表示 1.

number = input('输入整数：')
print(8>5 and 5!= int(number))

#位运算符
#二进制 0b开头 bin
a = 0b01001011 #二进制 0b开头
b = int(a) #二进制转换为十进制
print(b)
c = oct(a) #二进制转换为八进制
print(c)
d = hex(a) #二进制转换为十六进制
print(d)

e = bin(b)
print(e)

#八进制 0o开头
#十六进制 0x开头
#十进制

#三目运算符
result = '假' if (8>4)  else '真' #真取前面的值，假取后面的值。
result = '假' if (8>4)  else '真' #真取前面的值，假取后面的值。
a= 6
b= 5
result = 'a:{}>b:{}'.format(a,b) if (a>b) else 'a:{}<b:{}'
print(result)