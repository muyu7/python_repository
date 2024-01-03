from tkinter import *
from tkinter import ttk
from eventFuntions import EventFuntions
from feynmanElements import FeynmanElements
from globalVaribles import GlobalVariables
class UIController:
    def __init__(self) -> None:
        self.event = EventFuntions()
    def createBackground(self):
        glovars = GlobalVariables()
        canvas = glovars.get_canvas()

        # Ensure canvas dimensions are updated
        canvas.update_idletasks()

        canvasWidth=canvas.winfo_width()
        canvasHeight=canvas.winfo_height()
        gap = glovars.get_gap()

        # Draw vertical lines
        x=0
        while x*gap < canvasWidth:
            canvas.create_line(x*gap,0,x*gap,canvasHeight,fill='red')
            x += 1

        # Draw horizontal line
        y=0
        while y*gap < canvasHeight:
            canvas.create_line(0,y*gap,canvasWidth,y*gap,fill='red')
            y +=1

    # 创建工具栏
    def createMainBoard(self):
        glovars = GlobalVariables()
        root = glovars.get_root()
        if root == None:
            return
        # 生成顶部工具栏
        topFrm= Frame (root,height=50)
        topFrm.grid(column=0,row=0)
        ttk.Label(topFrm,text='Hello').grid(column=0,row=0)
        # 生成左边菜单栏
        leftFrm=ttk.Frame(root,width=50)
        leftFrm.grid(column=0,row=1)
        ttk.Button(leftFrm,text='draw straight line',command= lambda : self.event.OnStyleButtonClick(FeynmanElements.ElementStyle.STRAIGHT)).grid(column=0,row=0)
        # straigth_line_button.bind('<Button1>',)
        ttk.Button(leftFrm,text='draw wavy line',command= lambda : self.event.OnStyleButtonClick(FeynmanElements.ElementStyle.PHOTON)).grid(column=0,row=1)
        # create latex button
        ttk.Button(leftFrm,text='Latex',command= lambda : self.event.OnStyleButtonClick(FeynmanElements.ElementStyle.LATEX)).grid(column=0,row=2)
      
    def create_ui(self):
        self.createBackground()
        self.createMainBoard()
        self.bindEventToCanvas()

        self.event.reset_style()
    def bindEventToCanvas(self):
        glovars = GlobalVariables()
        canvas = glovars.get_canvas()
        canvas.bind('<ButtonPress-1>',lambda event:self.event.OnCanvasPress(event))
        canvas.bind('<B1-Motion>',lambda event:self.event.OnMouseMoving(event))
        canvas.bind('<ButtonRelease-1>',lambda event:self.event.OnCanvasRelease(event))

    