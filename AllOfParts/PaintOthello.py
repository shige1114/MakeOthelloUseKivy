from kivy.graphics import Color,Line
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget



class PaintOthello(Widget):
    def __init__(self,window_size,**kwargs,):
        super().__init__(**kwargs)
        self.size = (window_size[0]/3*2,window_size[1])
        self.line =[]
        with self.canvas:
            Color(0.5,0.2,0.1,1)
            self.rect = Rectangle(size =self.size ,pos=self.pos)
            for i in range(1,8):
                Color(0,0,0,1)
                self.line.append(Line(points=(0,self.size[1]/8*i,self.size[0],self.size[1]/8*i)))
                self.line.append(Line(points=(self.size[0]/8*i,0,self.size[0]/8*i,self.size[1],)))