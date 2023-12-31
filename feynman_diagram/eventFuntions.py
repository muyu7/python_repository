from feynmanElements import FeynmanElements
from globalVaribles import GlobalVariables

class EventFuntions:
    def __init__(self) -> None:
        self.feyEle = FeynmanElements()
        self.isClick = False
        self.old_line = None
    def changeisClick(self):
        if self.isClick:
            self.isClick = False
        else:
            self.isClick = True
    def OnStyleButtonClick(self, style:FeynmanElements.ElementStyle):
        self.feyEle.setElementStyle(style)

    def OnCanvasPress(self,event):
        if not self.isClick:
            self.feyEle.setPoints(event.x,event.y,-1,-1)
        else:
            return
    def OnMouseMoving(self,event):
        # print('OnMouseMoving')
        glovars = GlobalVariables()
        self.feyEle.setPoints(-1,-1,event.x,event.y)
        if self.old_line != None:
            glovars = GlobalVariables()
            canvas = glovars.get_canvas()
            canvas.delete(self.old_line)
        self.old_line = self.feyEle.draw_feynman_element(glovars.get_canvas())
    def OnCanvasRelease(self,event):
        glovars = GlobalVariables()
        self.feyEle.setPoints(-1,-1,event.x,event.y)
        self.feyEle.draw_feynman_element(glovars.get_canvas())

    def reset_style(self):
        self.feyEle.reset_style()
    