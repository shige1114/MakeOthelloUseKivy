#!/usr/bin/pyenv python
# # -*- coding: utf-8 -*-
__author__ = "HAMAGUCHI SHIGENAGA"
__date__ = 2022/2/22
__ver__ = "0.0.0"

from tkinter import Widget
from kivy.graphics import Color,Line,Ellipse
from BoardOfOthello import OthelloBoard

class PaintCircle:
    def __init__(self,widget,widget_size,):
        self.othello_board = OthelloBoard()
        self.window = widget
        self.widget_size_x,self.widget_size_y = widget_size
        
        self.circle_size_x = self.widget_size_x/8
        self.circle_size_y = self.widget_size_y/8

        self.circle_size = (self.circle_size_x,self.circle_size_y)

        self.window.on_touch_down

    def paint(self,turn,list_pos=None):
        x,y = list_pos
        print(x,y)
        pos = self.othello_board.board_pos[y][x]
        with self.window.canvas :
            if(turn):self.paint_white(pos)
            else:self.paint_black(pos)

    def paint_white(self,pos):
        Color(0,0,0)
        
        Ellipse(pos=pos,size=self.circle_size)

    def paint_black(self,pos): 
        Color(1,1,1)

        Ellipse(pos=pos,size=self.circle_size)

    
    def processing_pos(self,pos):
        x,y = pos
        pos_x = x//self.circle_size_x
        pos_y = y//self.circle_size_y 
        
        return (self.othello_board.board_pos[int(pos_x)][int(pos_y)])

     