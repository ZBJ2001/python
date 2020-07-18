'''
字符串的使用。
1、str[下标] ,下标不要越界
2、切片 不存在越界[start:end:step] 包前不包后 '[开始：结束：方向]
    一个完整的切片表达式包含两个“:”，用于分隔三个参数(start_index:end_index:step)。
    当只有一个“:”时，默认第三个参数step=1；当一个“:”也没有时，start_index=end_index，表示切取start_index指定的那个元素
    切片适用于列表,元组。

3、方法 系统内置方法
    index 查不到报错。
    find 返回-1
        Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，
        则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
        str.find(str, beg=0, end=len(string))
        参数
        str -- 指定检索的字符串
        beg -- 开始索引，默认为0。
        end -- 结束索引，默认为字符串的长度。

    rindex
    rfind 从右向左找到第一个符合的，索引还是按正常的索引值。
4、搜索\要转义。 \\
5、替换方法 replace（old,new,count) count替换个数 默认是全部
    Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。

    语法
    replace()方法语法：

    str.replace(old, new[, max])
    返回一个字串的copy

6、分割或切割：split split('分割符',最大次割次数) 返回的是列表。
    描述
    Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串

    语法
    split() 方法语法：

    str.split(str="", num=string.count(str)).

7、转换
    upper()转大写
    lower()转小写
    title()字符串的每个单词的首字母大写
    capitalize()字符串的第一个单词的首字母大写

8、字符串判断相关含数部分：
    1、isupper() 是否全是大写#ISCAR
    2、isLower() 是否全是小写
    3、isalpha() 是否字符串中只有字母，不包含数字或特殊符号，如果是返回true,否则返回false
    4、isDigitO()是否是纯数字。
    5、startsWith('符号') 是否以指定内容开头
    6、endswith() 是否以指定内容结尾。
9、对齐与格式  对方了解即可
    1、center() 在指定的宽度的正中间。
    2、ljust()  在指定宽度左对齐
    3、rjust()  在指定宽度右对齐

10、format格式化。最常用。另一种 %
    money = 5.99343434
    print('我有钱，现在有{:.2f}'.format(money)) #保留两位小数。
    {:.0f}不带小数。

11、去除空格
    strip() 去除字符串左右两边空格
    lstrip() 去除左侧空格
    rstrip() 去除右侧空格

12、字符串运算符
    +
    *
    in 内容 in 字符串 返回布尔。类似find
    not in
    is 两个字串判断地址是否相等，即判断对象。
    == 比较内容部分
    []下标符号，切片符号 。下标和切片是有区别的。
    % 字符串格式化

13、结合列表使用
    join
'''
import random  #导入模块

#切片练习
def fun1():
    str1 = 'hello world'
    #切取单个元素
    print('取{0}切片0'.format(str1), str1[0])
    print('取{0}切片-4'.format(str1), str1[-4])
    #切取完整元素
    print('#切取完整元素-------------')
    print('取{0}切片:: 从左至右'.format(str1), str1[::])
    print('取{0}切片::-1 从右至左'.format(str1), str1[::-1])
    #start_index和end_index全为正 索引情况
    print('#start_index和end_index全为正 索引情况-------------')
    print('取{0}切片0：5'.format(str1),str1[0:5])
    print('取{0}切片1:6:-1'.format(str1),str1[1:6:-1]) #无值，方向是右到左，索引是从左到右。矛盾。
    print('取{0}切片6：2'.format(str1),str1[6:2]) #无值，方向是左到右，索引是右到左，矛盾。
    print('取{0}切片：5'.format(str1),str1[:5]) #从起点到第5个 索引是5，0到4从左到右
    print('取{0}切片：6:-1'.format(str1),str1[:6:-1]) #从右到左，从终点到索引是6，不包括6

    #全为负
    print('全为负---------------')
    print('取{0}切片：-1:-6'.format(str1), str1[-1:-6])  #方向是左到右，索引是右到左，矛盾。是空值。
    print('取{0}切片：-1:-6：-1'.format(str1), str1[-1:-6:-1])  #方向是右到左，索引是右到左，索引从-1，起始，到-6止，不包括-6


    #多层切片
    print('取{0}多层切片：a[:8][2:5][-1:]'.format(str1), str1[:8][2:5][-1:])  #理论上可以无限多，只要上一次返回非空。
    #切片参数可以用表达式或变量
    b=3
    print('取{0}切片，用表达式'.format(str1),str1[b])



#内置函数练习
def fun2():
    str1 = '0123456789'
    #find练习
    print('--------->#find练习')
    print(str1.find('23')) #返回索引 2
    print(str1.find('02'))  # 返回索引 返回-1
    i = str1.find('3',-9,-1) #索引是负的也可以，但方向必须是从左到右。
    print(i)

    # index练习
    print('--------->#index练习')
    #print('{0} index zz'.format(str1),str1.index('zz')) #报错。
    print('{0} index 23'.format(str1),str1.index('23'))

    #rfind练习 从右向左找
    print('--------->#rfind练习 从右向左找到第一个符合的，索引还是按正常的索引值')
    print('{0} rfind 23'.format(str1),str1.rfind('23')) #

    #根据find返因索引数截字符串
    str1 = "http://www.hnwb.com.cn/forum/helloworld.jpg"
    index = str1.find('/',0)
    index = str1.find('/',index+1)
    str1[index+1:]


    print('字符串{0}查看/的索引是:'.format(str1),index)
    print(str1[index+1:])

    #replace练习
    str1 = 'hello 帅哥,hi 帅哥'
    str1 = str1.replace('帅哥', '美女', 1)

    print(str1.replace('hnwb','HNWB'),str1)

    #split练习
    str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
    print (str.split())  # 以空格为分隔符，包含 \n
    print (str.split(' ', 1))  # 以空格为分隔符，分隔成两个

    # split
    s = r'E:\安装程序\Python开发\python官方帮助文档\python官方帮助文档'
    list = s.split('\\')  # 返回的是列表
    print(list)

#字符串转换练习
def fun3():
    '''
    7、转换     upper()    转大写    lower()    转小写    title()    字符串的每个单词的首字母大写    capitalize()    字符串的第一个单词的首字母大写

    8、字符串判断相关含数部分：
    1、isupper()    是否全是大写  # ISCAR
    2、isLower()    是否全是小写
    3、isalpha()    是否字符串中只有字母，不包含数字或特殊符号，如果是返回true, 否则返回false
    4、isDigitO()    是否是纯数字。
    5、startsWith('符号')    是否以指定内容开头
        startswith()方法语法：

        str.startswith(str, beg=0,end=len(string));
        参数
        str -- 检测的字符串。
        strbeg -- 可选参数用于设置字符串检测的起始位置。
        strend -- 可选参数用于设置字符串检测的结束位置。 (包前包不后。）

    6、endswith()    是否以指定内容结尾。
    :return: 
    '''
    str1 = 'Hello world'
    str1.upper()  #返回一个copy
    print('{0} 应用upper() 结果是{1}'.format(str1,str1.upper()))
    print('{0} 应用capitalize() 结果是{1}'.format(str1,str1.capitalize()))
    print('{0} 应用title() 结果是{1}'.format(str1,str1.title()))
    print('{0} 应用lower() 结果是{1}'.format(str1,str1.lower()))

    print("{0} 应用str1.startswith('He') 结果{1}".format(str1,str1.startswith('He')))

    print("{0} 应用str1.startswith('l',2,4) 结果{1}".format(str1,str1.startswith('l',2,4)))
    print("{0} 应用str1.startswith('o',2,4) 结果{1}".format(str1,str1.startswith('o',2,4)))
    print("{0} 应用str1.startswith('o',4,5) 结果{1}".format(str1,str1.startswith('o',4,5)))

    print("{0} 应用str1.endswith('ld') 结果{1}".format(str1,str1.endswith('ld')))
    print("{0} 应用str1.endswith('lo',3,4) 结果{1}".format(str1,str1.endswith('lo',3,4)))
    print("{0} 应用str1.endswith('lo',3,5) 结果{1}".format(str1,str1.endswith('lo',3,5)))

    print("{0} .isalpha() 结果{1}".format('890a','890a'.isalpha()))
    print("{0} .isdigit() 结果{1}".format('890','890'.isdigit()))


#实际应用练习

def fun4():
    # 验证码练习
    code = ''
    base_str = '1234adjfksadjfklasdhkjasdkfjsadkjfASDJFKLASDJFKASDJFKLJASDFKLJ12341234ASDFasdfkasdjf';
    for i in range(0, 4):
        r = random.randint(0, len(base_str) - 1)  # randint(包前，包后）。其他大多数含数是包前不包后的。
        code += base_str[r]
    print('验证码：', code)


    # 纯数字，长度5-10，不能以0开头
    qq = '1345345343'
    # if qq.isdigit() and len(qq)>=5 and len(qq)<=10 and not qq.startswith('0'):
    if qq.isdigit() and 10 >= len(qq) >= 5 and not qq.startswith('0'):

        print('qq号码符合规范')
    else:
        print('qq号码不符合规范')


    # 文件上传，只能上传（png,jpg,gif)
    file = '文件名.jpg'
    if file.endswith('.jpg'):
        print('图片格式，允许上传')

    str1 = 'hello world'
    print(str1.center(100))  # 在100的宽度的正中间。

    #format练习
    name = '蔡徐坤'
    age = 22
    gender='男'
    print('00后很喜欢明星是：{},今年{}岁,性别:{}'.format(name,age,gender)) #这是调用字符串的内雷函数。

    print('00后很喜欢明星是：{name},今年{age}岁,性别:{gender}'.format(name=name,age=age,gender=gender)) #这是调用字符串的内雷函数。
    print('00后很喜欢明星是：{a},今年{b}岁,性别:{c}'.format(a=name,b=age,c=gender)) #这是调用字符串的内雷函数。

    print('00后很喜欢明星是：{1},今年{0}岁,性别:{2}'.format(name,age,gender)) #这是调用字符串的内雷函数。
    money = 5.99343434
    print('我有钱，现在有{:.2f}'.format(money)) #保留两位小数。
    #{:.0f}不带小数。

fun4()
exit() #退出当前模块












