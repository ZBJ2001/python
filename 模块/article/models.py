class Article:
    def __init__(self,name,author):
        self.name = name
        self.author = author

    def show(self):
        print('发表文章名字：{}，作者是：{}'.format(self.name,self.author))


class Tag:
    def __init__(self,name):
        self.name = name


print('-----------> models.py 执行命令')