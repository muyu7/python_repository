import tkinter as tk
import math
import numpy as np
from globalVaribles import GlobalVariables

class FeynmanElements:
    class ElementStyle:
        NONE = 'none'
        PHOTON = 'photon'
        STRAIGHT = 'straight'
    def __init__(self) -> None:
        self.elementStyle = self.ElementStyle.NONE

        self.amplitude = 7
        self.wavelength =40
        self.steps = 1000
        self.lineWidth = 3

        self.start_x =-1
        self.start_y =-1
        self.end_x =-1
        self.end_y =-1
        self.is_line_changed = False

        self.old_line=None
    def set_start_points(self,start_x, start_y):
        
        start_point = self.get_vaild_point(start_x,start_y)
        print('points2:',self.start_x,start_point[0],self.start_y,start_point[1])
        if self.start_x == start_point[0] and self.start_y == start_point[1]:
            self.is_line_changed = False
            return
        else:
            self.is_line_changed = True
        if start_point[0] != -1:
            self.start_x = start_point[0]
        if start_point[1] != -1:
            self.start_y = start_point[1]
    def set_end_point(self,end_x,end_y):
        end_point = self.get_vaild_point(end_x, end_y)
        if self.end_x == end_point[0] and self.end_y == end_point[1]:
            self.is_line_changed = False
            return
        else:
            self.is_line_changed = True
        
        if end_point[0] != -1:
            self.end_x = end_point[0]
        if end_point[1] != -1:
            self.end_y = end_point[1]
    def reset_style(self):
        self.elementStyle = self.ElementStyle.NONE
    def reset_old_line(self):
        self.old_line = None
    def setElementStyle(self, style:ElementStyle):
        if style not in (self.ElementStyle.PHOTON, self.ElementStyle.STRAIGHT):
            raise ValueError("Invalid style. Must be an ElementStyle.")
        self.elementStyle = style
    def draw_wavy_line(self, canvas, start_x, start_y, end_x, end_y):
        # Check for horizontal line
        if start_y == end_y:
            end_x_rotation = end_x
            rotationMatrix = self.calculateTurnMatrix(start_x, start_y, end_x, end_y)
        else:
            # 把终点旋转到与起点同一水平线上
            rotationMatrix = self.calculateTurnMatrix(start_x, start_y, end_x, end_y)
            rotationMatrix_inver= np.linalg.inv(rotationMatrix)
            end_x_rotation = rotationMatrix_inver.dot([end_x-start_x,end_y-start_y])[0]+start_x
        # Calculate the length of the line
        length = end_x_rotation - start_x

        if length == 0:  # Check for very short lines
            return
        half_wave_num = round (2 * length / self.wavelength)
        local_wavelength = length /(half_wave_num*2)
        # Calculate the horizontal distance between points (step size)
        step_size = length / self.steps

        # Initialize an empty list for points
        points = []
        # Loop to calculate points along the wavy line
        for i in range(self.steps + 1):
            # Calculate the x coordinate
            x = start_x + i * step_size
            # Calculate the y coordinate using a sinusoidal function
            y = start_y + self.amplitude * math.sin(2 * math.pi * i*step_size / local_wavelength)
            # print('x:',x,'y',y)
            # 旋转到需要的位置
            rotatePoint = rotationMatrix.dot([x-start_x,y-start_y]) + [start_x,start_y]

            # Append the point to the list
            points.extend(rotatePoint)
        # Draw the wavy line using the calculated points
        return canvas.create_line(points, smooth=True, width=self.lineWidth)
    def calculateTurnMatrix(self, start_x, start_y, end_x, end_y):
        delta_x = end_x - start_x
        delta_y = end_y - start_y
        if delta_x == 0:  # Vertical line
            angle = math.pi / 2
        else:
            angle = math.atan2(delta_y, delta_x)
        turningMatrix = np.array([[np.cos(angle),-np.sin(angle)],[np.sin(angle),np.cos(angle)]])
        return turningMatrix
    def draw_straight_line(self, canvas, start_x, start_y, end_x, end_y):
        length = self.calculate_distance(start_x, start_y, end_x, end_y)
        if length ==0:
            return
        else:
            return canvas.create_line(start_x, start_y, end_x, end_y, smooth=True, width=self.lineWidth)
    def calculate_distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    def draw_feynman_element(self, canvas):
        if self.elementStyle == FeynmanElements.ElementStyle.NONE:
            return
        if not self.is_line_changed :
            return
        print('point changed',self.is_line_changed)
        if self.start_x == -1 or self.start_y == -1 or self.end_x == -1 or self.end_y == -1:
            return
        
        if self.old_line != None:
            canvas.delete(self.old_line)

        match self.elementStyle:
            case self.ElementStyle.PHOTON:
                self.old_line = self.draw_wavy_line(canvas, self.start_x, self.start_y, self.end_x, self.end_y)
            case self.ElementStyle.STRAIGHT:
                self.old_line = self.draw_straight_line(canvas, self.start_x, self.start_y, self.end_x, self.end_y)
            case _:
                return
    def get_vaild_point(self, x, y):
        if x == -1 or y == -1:
            return [x,y]
        glovars = GlobalVariables()
        gap = glovars.get_gap()
        canvas = glovars.get_canvas()
        max_x = math.floor(canvas.winfo_width() / gap)
        max_y = math.floor(canvas.winfo_height() / gap)
        num_x = min(round(x / gap),max_x)
        num_y = min(round(y / gap),max_y)
        return [num_x*gap,num_y*gap]  

