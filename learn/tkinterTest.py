from tkinter import *
from tkinter import ttk


# 输出日志
def log(event):
    print(event.widget.find_withtag('current')[0].configure().key())
# 画一条直线

def drawLine(canvas):
    #line = canvas.create_line(100, 100, 300, 25, width=5)
    #print(type(getCurrentItem))
    # 画布拖拽
    #line = canvas.bind('<B1-Motion>',lambda event: getCurrentItem)
    # 画布点击
    canvas.bind('<ButtonPress-1>',lambda event:getCurrentItem(event,canvas))
    #line = canvas.tag_bind('lines1','<B1-Motion>',lambda event: refreshLine(event,canvas,line))
    # 点击lines
    #line = canvas.tag_bind('lines1','<ButtonPress-1>',log)
    # canvas.focus()
    # canvas.pack()
    return canvas
def refreshLine(event,canvas,oldLine):
    canvas.create_line(event.x, event.y, 200, 25, width=5)
def difineGlobalVarities():
    global activeItemId
    activeItemId=None
    print('difineGlobalVarities=',activeItemId)
def onButton1Press(event,canvas):
    global activeItemId
    pressPosX=event.x
    pressPosY=event.y
    activeItemId = canvas.create_line(pressPosX,pressPosY,pressPosX,pressPosY,width=5)
    print('buttonPress id=',activeItemId)
def onButton1Moving(event,canvas):
    global activeItemId
    print('moving id=',activeItemId)
    oldPos=canvas.coords(activeItemId)
    canvas.coords(activeItemId,oldPos[0],oldPos[1],event.x,event.y)
#def onButtonlift(event.canvas):
def bindEventToCanvas():
    canvas.bind('<ButtonPress-1>',lambda event:onButton1Press(event,canvas))
    canvas.bind('<B1-Motion>',lambda event:onButton1Moving(event,canvas))
    

    
    

def getCurrentItem(event,canvas):
    #currentItemsId = event.widget.find_withtag('current')
    
    currentItemsId = event.widget.find_closest(event.x,event.y)
    # for i in currentItemsId:
    #     print(canvas.coords(i))
    
    # for widget in currentItems:
    #     if()
# 创建canvas背景
def creatbackground(canvas):
    x=0
    canvasWidth=canvas.winfo_width()
    canvasHeight=canvas.winfo_height()
    gap=20
    while x*gap < canvasWidth:
        canvas.create_line(x*gap,0,x*gap,canvasHeight,fill='red')
        x=x+1
    y=0
    while y*gap < canvasWidth:
        canvas.create_line(0,y*gap,canvasWidth,y*gap,fill='red')
        y=y+1
# 创建工具栏
def creatMainBoard(root,canvas):
    # 生成顶部工具栏
    topFrm=Frame(root,height=50)
    topFrm.grid(column=0,row=0)
    ttk.Label(topFrm,text='Hello').grid(column=0,row=0)
    # 生成左边菜单栏
    leftFrm=ttk.Frame(root,width=50)
    leftFrm.grid(column=0,row=1)
    ttk.Button(leftFrm,text='drawLine',command=difineGlobalVarities()).grid(column=0,row=0)
    
        
root = Tk()
canvas = Canvas(root,width=800,height=800,background='white')
canvas.focus()
canvas.grid(column=1,row=1)
canvas.update()
difineGlobalVarities()
creatMainBoard(root,canvas)
creatbackground(canvas)
bindEventToCanvas()
# line=drawLine(canvas)
# line.grid(column=0,row=0)
# frm = ttk.Frame(root,padding=(50,10,100,30))
# frm.grid(column=0,row=0)
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="draw it", command=root.destroy).grid(column=1, row=0)
root.mainloop()

# 找到点击的对象
# event.widget.find_withtag('current')[0]
# event.widget.find_closest(event.x, event.y) # 当有重叠对象时,这个方法可能处理起来很麻烦

# test for tkinter
# import tkinter as tk
# from tkinter import TclError, ttk


# def create_input_frame(container):

#     frame = ttk.Frame(container)

#     # grid layout for the input frame
#     frame.columnconfigure(0, weight=1)
#     frame.columnconfigure(0, weight=3)

#     # Find what
#     ttk.Label(frame, text='Find what:').grid(column=0, row=0, sticky=tk.W)
#     keyword = ttk.Entry(frame, width=30)
#     keyword.focus()
#     keyword.grid(column=1, row=0, sticky=tk.W)

#     # Replace with:
#     ttk.Label(frame, text='Replace with:').grid(column=0, row=1, sticky=tk.W)
#     replacement = ttk.Entry(frame, width=30)
#     replacement.grid(column=1, row=1, sticky=tk.W)

#     # Match Case checkbox
#     match_case = tk.StringVar()
#     match_case_check = ttk.Checkbutton(
#         frame,
#         text='Match case',
#         variable=match_case,
#         command=lambda: print(match_case.get()))
#     match_case_check.grid(column=0, row=2, sticky=tk.W)

#     # Wrap Around checkbox
#     wrap_around = tk.StringVar()
#     wrap_around_check = ttk.Checkbutton(
#         frame,
#         variable=wrap_around,
#         text='Wrap around',
#         command=lambda: print(wrap_around.get()))
#     wrap_around_check.grid(column=0, row=3, sticky=tk.W)

#     for widget in frame.winfo_children():
#         widget.grid(padx=5, pady=5)

#     return frame


# def create_button_frame(container):
#     frame = ttk.Frame(container)

#     frame.columnconfigure(0, weight=1)

#     ttk.Button(frame, text='Find Next').grid(column=0, row=0)
#     ttk.Button(frame, text='Replace').grid(column=0, row=1)
#     ttk.Button(frame, text='Replace All').grid(column=0, row=2)
#     ttk.Button(frame, text='Cancel').grid(column=0, row=3)

#     for widget in frame.winfo_children():
#         widget.grid(padx=5, pady=5)

#     return frame


# def create_main_window():
#     root = tk.Tk()
#     root.title('Replace')
#     root.resizable(0, 0)
#     try:
#         # windows only (remove the minimize/maximize button)
#         root.attributes('-toolwindow', True)
#     except TclError:
#         print('Not supported on your platform')

#     # layout on the root window
#     #root.columnconfigure(0, weight=4)
#     #root.columnconfigure(1, weight=1)

#     input_frame = create_input_frame(root)
#     input_frame.grid(column=0, row=0)

#     button_frame = create_button_frame(root)
#     button_frame.grid(column=1, row=0)

#     root.mainloop()


# if __name__ == "__main__":
#     create_main_window()
