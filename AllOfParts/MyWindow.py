from cProfile import label
from tkinter import Grid
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from BoardOfOthello import PaintOthello
from kivy.core.window import Window
from PaintCircle import PaintCircle
from MouseControll import MouseControll

class MyWindow(FloatLayout):
    def __init__(self, **kwargs):
        self.window_size = Window.size
        self.othello_board_x = self.window_size[0]/3*2
        self.othello_board_y = self.window_size[1]
        
        super().__init__(**kwargs)
        self.mouse_controll = MouseControll(circle_size_x=self.othello_board_x,circle_size_y=self.othello_board_y)
        self.board = PaintOthello(size = (self.x,self.y),pos=(0,0),window_size=self.window_size)
        self.paint_circle = PaintCircle(widget=self.board,widget_size=(self.othello_board_x,self.othello_board_y))
        self.add_widget(self.board,)
        self.add_widget(self.mouse_controll)
        self.add_widget(Button(text='World 1',size=(self.othello_board_x/2,100), pos=(self.othello_board_x,6)),)
        self.paint_circle.paint(list_pos=(3,3),turn=True)
        self.paint_circle.paint(list_pos=(3,4),turn=False)
        self.paint_circle.paint(list_pos=(4,3),turn=False)
        self.paint_circle.paint(list_pos=(4,4),turn=True)
        if(self.mouse_controll.is_touch):
            print("Mouse")
            self.paint_circle.paint(list_pos=self.mouse_controll.mouse_pos,turn=False)

    def on_touch_down(self, touch):
        x,y = touch.pos
        pos = self.processing_pos(x,y)
        self.paint_circle.paint(list_pos=pos,turn=False)
        return super().on_touch_down(touch)
    
    def processing_pos(self,x,y):
        
        pos_x = x//(self.othello_board_x/8)
        pos_y = y//(self.othello_board_y/8)
        print(pos_x,pos_y)
        return (int(pos_x),int(pos_y))
        
    
        

        

