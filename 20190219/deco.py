

def set_color(func):  #这个函数的作用是制造某个功能的函数（功能：调用第三个函数 取得这个函数的返回值  来赋颜色）
    def color():
        return "\033[31;1m%s\033[0m" % func()
    return color

def hello():
    return 'hello world！'

@set_color
def welcome():
    return 'hello china!'




if __name__ == '__main__':
    # a = set_color(hello)
    # print(a())
    # a = set_color(welcome)
    # print(a())

    hello=set_color(hello)
    print(hello())

    print(welcome)     #调用set_color(welcome)  返回内层函数color
    print(welcome())    #此处的调用  实际上是调用内层的color