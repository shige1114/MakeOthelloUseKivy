#!/usr/bin/pyenv python
# # -*- coding: utf-8 -*-
__author__ = "HAMAGUCHI SHIGENAGA"
__date__ = 2022/2/22
__ver__ = "0.0.0"

from kivy.graphics import Color,Line,Ellipse


class PaintCircle:
    def __init__(self,widget,widget_size,):
        self.window = widget
        self.widget_size_x,self.widget_size_y = widget_size
        
        self.circle_size_x = self.widget_size_x/8-5
        self.circle_size_y = self.widget_size_y/8-5
        self.circle_size = (self.circle_size_x,self.circle_size_y)

        self.window.on_touch_down

    def paint(self,turn,list_pos=None):
        
        with self.window.canvas :
            if(turn):self.paint_white(list_pos)
            else:self.paint_black(list_pos)

    def paint_white(self,pos):
        Color(0,0,0)
        Ellipse(pos=pos,size=self.circle_size)
        
    def paint_black(self,pos): 
        Color(1,1,1)        
        Ellipse(pos=pos,size=self.circle_size)

    def clear_circle(self,pos):
        with self.window.canvas:
            Color(0.5,0.2,0.1,1)
            Ellipse(pos=pos,size=self.circle_size)

    def board_update(self,**args):
        for y in range(len(args["board"])):
            for x in range(len(args["board"][y])):
                if(args["board"][y][x]==args["turn"]):self.paint(list_pos=args["board_pos"][y][x],turn=args["turn"])
