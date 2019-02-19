
import tkinter

from functools import partial

window=tkinter.Tk()

lb=tkinter.Label(window,text='hello world')

MyButton = partial(tkinter.Button,window,fg='white',bg='blue')

b1=MyButton(text='qiaoxin')
b2=MyButton(text='linlin')
b3=MyButton(text='qihl')

for item in (lb,b1,b2,b3):
    item.pack()    #把4个组件安装到window上


window.mainloop()  #主程序方法