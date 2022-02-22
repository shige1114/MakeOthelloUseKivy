from curses import window
from tkinter import Label
from kivy.graphics import Color,Line
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.core.window import Window


class PaintOthello(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.size = (Window.size[0]/3*2,Window.size[1])
        self.line =[]
        with self.canvas:
            Color(0,1,0,1)
            
            self.rect = Rectangle(size =self.size ,pos=self.pos)
            for i in range(1,8):
                Color(1,1,1,1)
                self.line.append(Line(points=(0,self.size[1]/8*i,self.size[0],self.size[1]/8*i)))
                self.line.append(Line(points=(self.size[0]/8*i,0,self.size[0]/8*i,self.size[1],)))

            
class OthelloBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)]for _ in range(8)]        
        self.turn = True
        
    def paint_circle(self,):
        if(self.turn):
            self.turn_update()
        else:
            self.turn_update()

    def turn_update(self):
        if(self.turn):self.turn=False
        else:self.turn=True


    