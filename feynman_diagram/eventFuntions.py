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
            self.feyEle.set_start_points(event.x,event.y)
        else:
            return
    def OnMouseMoving(self,event):
        # print('OnMouseMoving')
        glovars = GlobalVariables()
        self.feyEle.set_end_point(event.x,event.y)
        self.old_line = self.feyEle.draw_feynman_element(glovars.get_canvas())
    def OnCanvasRelease(self,event):
        glovars = GlobalVariables()
        self.feyEle.reset_old_line()
        self.feyEle.set_end_point(event.x,event.y)
        self.feyEle.draw_feynman_element(glovars.get_canvas())

    def reset_style(self):
        self.feyEle.reset_style()
    