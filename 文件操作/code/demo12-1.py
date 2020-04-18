'''
文件操作


mode: r w
        rb wb
    纯文本文件
    r:read  读操作
    w:write 写操作
    a：append   追加模式
    纯文本，图片，音乐 ，视频。
    b:binary 二进制
    rb,wb

    缓存：
        硬件和CPU缓冲。4096、8192
    系统函数
    open(file,mode,buffering,encodeing)
    rt 如果是方本，默认方式
    rb 图片 用这个方式。
    read() #读取所有内容。
    readline() #每次读一行
    readlines() #读所有的行放在列表中
    readable() #判断 是否可读

    方法：
    write(内容） 每次都会将原来的内容清空。

    文件的复制

    with 结合Open使用，帮助我们自动释放资源。

    os模块
    os.path.dirname(__file__) 返回当前目录
    os.path.join(path,'') 返回拼接
    absolute 绝对路径
    isabs() 测试是否绝对路径
    相对路径。

'''
import os
import ntpath

# stream = open(r'E:\python\文件操作\aa.txt')

# container = stream.read()
# result = stream.readable() #判断是否可以读取。
# print(container)

# while True:
#     line = stream.readline()#一行一行的读 自动换行
#     print(line)
#     if not line:
#         break
#
# stream.seek(0,0) #复位
#
# lines = stream.readlines() #保存在列表中。
# print(lines)
# stream.close()
# #写文件 会把原内容覆盖掉
# s='''
#     你好！
#         欢迎来到澳门博彩赌场，赠送给你一个金币！
#                             财神：高进
#     '''
# stream = open(r'E:\python\文件操作\aa.txt','w')
# if stream.writable():#能不能写
#     result = stream.write(s) #返回写入的字节数
#     stream.write('龙五')
#
#     stream.writelines('财神高进\n')
#     stream.writelines(['张宝军\n','张潇\n','张宇瑞\n'])
#
#
#
#     stream.close()


# stream = open(r'E:\python\文件操作\aa.txt')
#
# # container = stream.read()
# # result = stream.readable() #判断是否可以读取。
# print(stream.read())

#复制练习
def fun1():
    with open(r'../images/1.jpg', 'rb') as stream:
        container = stream.read() #读取文件内容

    with open(r'E:\python\文件操作\2.jpg','wb') as wstream:
        wstream.write(container)
    print('文件复制完成！')

#复制目录下所有文件练习
def fun2():
    path = os.path.dirname(__file__) #获取当前文件所在的文件目录 绝对路径
    print(path)

    #返回上级 ../跳到上一级.
#OS.PATH学习
def fun3():

    '''
        os.path常用函数
        dirname()
        join()
        split()
        splittext()
        getsize()
        isabs()
        isfile()
        isdir()
    :return:
    '''
    #isabs()判断路径是绝对还是相对。
    print(os.path.isabs(r'E:\p1\1.txt'))
    print(os.path.isabs('../images/1.jpg')) #../ 返回上一级.
    #获取路径

    # 获取当前文件所在的文件目录 绝对路径
    path = os.path.dirname(__file__)
    print(path)

    # 获得指定文件的绝对路径。
    path= os.path.abspath('demo12-1.py')
    print(path)

    #获取当前文件的绝对路径
    path = os.path.abspath(__file__)
    print(path)

    # 获取当前文件所在的文件目录 绝对路径
    path=os.getcwd()
    print(path)

    r= os.path.isfile(os.getcwd())
    print('os.path.isfile(os.getcwd())---->',r)
    r=os.path.isdir(os.getcwd())

    print('os.path.isdir(os.getcwd())---->',r)

    result = os.path.split(__file__)
    print('os.path.split(__file__)---->',result)

    filename=__file__
    print(filename[filename.rfind('/')+1:]) #得到文件名

    print('__file__----->',__file__)

    result = os.path.splitext(__file__)  #文件扩展名
    print('os.path.splitext(__file__)---->',result)

    result = os.path.getsize(__file__) #获取文件大小,单位是字节.
    print('os.path.getsize(__file__)---->', result)

    result = os.path.join(os.getcwd(),'file','a1.txt')
    print("os.path.join(os.getcwd(),'file','a1.txt')---->", result)


#os中函数。
def fun4():
    '''
        os.getcwd() #获取当前目录
        os.listdir()    #当前文件夹文件生成列表
        os.mkdir()  #创建文件夹
        os.rmdir()  ##删除空的文件夹
        os.remove() #删除文件
        os.chdir() #切换目录


    :return:
    '''
    print('os.getcwd()----->',os.getcwd()) #当前目录
    print('os.listdir(os.getcwd()----->', os.listdir(os.getcwd()))  # 当前目录



    # if not os.path.exists(r'e:/p3/p4'): #判断文件夹是否存在
    #     result = os.mkdir(r'e:\p3/p4')  # 创建目录

    # os.rmdir(r'e:\p3\p4') #删除目录 ，只能删除空文件夹。

 #   r= os.removedirs('e:/p3') #删除多层目录。
 #   print('删除成功---->',r)

    #os.remove('../../../p3/p4/aa.txt') #删除文件

    # path = 'e:/p3/p4'
    # if not os._exists(path): return
    # filelist = os.listdir(path)
    # for file in filelist:
    #     filefullname = os.path.join(path,file)
    #     os.remove(filefullname)
    # else:
    #     os.rmdir(path)
    # print('{0}删除成功',path)

    #切换目录
    os.chdir('c:') #改变目录
    print(os.getcwd()) #获取当前路径

#文件复制
src = 'e:/p1'
target = 'e:/p2'
def copy(src,target):
    if os.path.isdir(src) and os.path.isdir(target):
        filelist = os.listdir(src)
        for file in filelist:
            filefullname = os.path.join(src,file)
            with open(filefullname,'rb') as rstream:
                container = rstream.read()
                tarfullname = os.path.join(target,file)
                with open(tarfullname,'wb') as wstream:
                    wstream.write(container)
        else:
            print('文件复制完成！')
    else:
        print('参数不是目录，无法复制！')


def copywithdir(src,target):
    # print(os.listdir(src))
    for file in os.listdir(src):
        path = os.path.join(src,file)
        if os.path.isdir(path):
            os.mkdir(os.path.join(target,file))
            copywithdir(os.path.join(src,file),os.path.join(target,file))
        else:
            with open(path,'rb') as rstream:
                container = rstream.read()
                tarfullname = os.path.join(target,file)
                with open(tarfullname,'wb') as wstream:
                    wstream.write(container)

copywithdir(src,target)
exit()