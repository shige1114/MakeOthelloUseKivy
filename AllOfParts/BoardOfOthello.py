from kivy.graphics import Color,Line
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.core.window import Window


class PaintOthello(Widget):
    def __init__(self,window_size,**kwargs,):
        super().__init__(**kwargs)
        self.size = (window_size[0]/3*2,window_size[1])
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
        self.size = Window.size
        self.Othello_x = self.size[0]/3*2
        self.Othello_y = self.size[1]
        self.board_pos = [[() for _ in range(8)]for _ in range(8)]
        self.board_pos = self.make_board_pos(self.board_pos)

    def paint_circle(self,):
        if(self.turn):
            self.turn_update()
        else:
            self.turn_update()

    def turn_update(self):
        if(self.turn):self.turn=False
        else:self.turn=True

    def make_board_pos(self,pos_list):
        a_mas_x=self.Othello_x/8
        a_mas_y=self.Othello_y/8
        for y in range(8):
            for x in range(8):
                pos_list[y][x] = (a_mas_x*x,a_mas_y*y)

        return pos_list

    def judge_sandwich(self):
        pass

    def judge_place_koma(self):
        pass