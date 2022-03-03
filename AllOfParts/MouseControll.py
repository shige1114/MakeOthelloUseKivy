from tkinter.messagebox import NO
from kivy.uix.widget import Widget


class MouseControll(Widget):

    def __init__(self,circle_size_x,circle_size_y, **kwargs):
        super(MouseControll,self).__init__(**kwargs)
        self.circle_size_x = circle_size_x/8
        self.circle_size_y = circle_size_y/8
        self.is_touch = False
        self.mouse_pos = []
        self.befor_pos = None

    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        
        self.is_touch=True
        self.befor_pos = touch.pos
        self.mouse_pos=self.processing_pos(self)

    def on_touch_up(self, touch):
        self.is_touch = False

    def processing_pos(self,x):
        x,y = self.befor_pos
        self.befor_pos=None
        pos_x = x//self.circle_size_x
        pos_y = y//self.circle_size_y
      
        return (int(pos_x),int(pos_y))
        
        