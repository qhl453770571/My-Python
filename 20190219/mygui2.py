
import tkinter

from functools import partial

# def qiaoxin():
#     lb.config(text='hello qiaoxin')
#
# def linlin():
#     lb.config(text='hello linlin')

def say_hi(word):
    def greet():
        lb.config(text="hello %s" % word)
    return greet


window=tkinter.Tk()

lb=tkinter.Label(window,text='hello world')

MyButton = partial(tkinter.Button,window,fg='white',bg='blue')

b1=MyButton(text='qiaoxin',command=say_hi('china'))
b2=MyButton(text='linlin',command=say_hi('tedu'))
b3=MyButton(text='quit',command=window.quit)

for item in (lb,b1,b2,b3):
    item.pack()    #把4个组件安装到window上


window.mainloop()  #主程序方法