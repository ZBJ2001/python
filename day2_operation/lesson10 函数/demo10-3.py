'''
函数相互调用。

'''
books = ['红楼梦','西游记','水浒传','三国演义']
def show_book():
    print('-----图书馆书籍如下-------')
    for index,book in enumerate(books):
        print('{}:{}'.format(index+1,book))

def add_book(book_name):
    if book_name:  # '' none 0 都为FALSE
        books.append(book_name)
        #确认是否成功
        show_book()
    else:
        print('书籍不能为空！')

add_book('斩龙')