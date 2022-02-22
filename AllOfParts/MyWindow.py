from cProfile import label
from tkinter import Grid
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from BoardOfOthello import PaintOthello
from kivy.core.window import Window

class MyWindow(FloatLayout):
    def __init__(self, **kwargs):
        self.size = Window.size
        self.x = self.size[0]/3*2
        self.y = self.size[1]
        print(self.x,self.y)
        super().__init__(**kwargs)
        self.rows = 1
        self.cols = 2
        self.board = PaintOthello(size = (self.x,self.y),pos=(0,0))
        self.add_widget(self.board, )
        self.add_widget(Button(text='World 1',size=(self.x/2,100), pos=(self.x,6)),)
        

        

