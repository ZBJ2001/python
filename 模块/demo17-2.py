'''
包导入

        文件夹放非py文件
        包放py文件 。
        区别就是__init__.py文件

项目-包-模块-类/函数/变量

from 包名 import 模块
from 包名.模块名 import 成员

__init__.py的作用。


'''
import user
# from user.models import User

from article.models import Article
article = Article('个人总结','zbj')

user.create_app()
user.printA()
