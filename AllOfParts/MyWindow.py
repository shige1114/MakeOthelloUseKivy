from cProfile import label
from tkinter import Grid
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from BoardOfOthello import PaintOthello
from kivy.core.window import Window
from PaintCircle import PaintCircle

class MyWindow(FloatLayout):
    def __init__(self, **kwargs):
        self.size = Window.size
        self.Othello_x = self.size[0]/3*2
        self.Othello_y = self.size[1]
        
        super().__init__(**kwargs)
        
        self.board = PaintOthello(size = (self.x,self.y),pos=(0,0))
        self.paint_circle = PaintCircle(widget=self.board,widget_size=(self.Othello_x,self.Othello_y))
        self.add_widget(self.board,)

        self.add_widget(Button(text='World 1',size=(self.Othello_x/2,100), pos=(self.Othello_x,6)),)
        self.paint_circle.paint(list_pos=(4,4),turn=True)
        self.paint_circle.paint(list_pos=(4,4),turn=False)
        

        

