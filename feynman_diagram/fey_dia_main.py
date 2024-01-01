from tkinter import *
from tkinter import ttk
from uiController import UIController
from feynmanElements import FeynmanElements
from globalVaribles import GlobalVariables

root = Tk()
canvas = Canvas(root,width=800,height=800,background='white')
canvas.grid(column=1,row=1)

gloVar = GlobalVariables()
gloVar.set_root(root)
gloVar.set_canvas(canvas)

ui_controller = UIController()
ui_controller.create_ui()

root.mainloop()
