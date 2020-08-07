'''
包导入

        文件夹放非py文件
        包放py文件 。
        区别就是__init__.py文件

项目-包-模块-类/函数/变量

from 包名 import 模块
from 包名.模块名 import 成员

'''

from article.models import Article

import article

from article import *

from 模块.calculate import add
from 模块.article.models import Article

from 模块.article.models import *
from 模块.article.models import Article

print(add(3, 4, 5))
print(Article('zbj', 'zbj'))
