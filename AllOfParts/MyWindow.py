from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from TextWidget import TextWidget
from BoardOfOthello import OthelloBoard
from PaintOthello import PaintOthello
from kivy.core.window import Window
from PaintCircle import PaintCircle

class MyWindow(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.othello_board = OthelloBoard()
        self.is_touch = False
        self.window_size = Window.size
        self.is_first_touch = True
        self.othello_board_x = self.window_size[0]/3*2
        self.othello_board_y = self.window_size[1]

        self.start_button_x = self.window_size[0]/3
        self.start_button_y = self.window_size[1]/3

        self.text_widget_size=(self.window_size[0]/3,self.window_size[1]/3*2)
        
        self.board = PaintOthello(size = (self.othello_board_x,self.othello_board_y),pos=(0,0),window_size=self.window_size)
        self.paint_circle = PaintCircle(widget=self.board,widget_size=(self.othello_board_x,self.othello_board_y))
        self.start_button = Button(text="Start",size=(self.start_button_x,self.start_button_y),size_hint=(None, None), pos=(self.othello_board_x,0))
        self.text_widget = TextWidget(text="Start!",widget_size=self.text_widget_size,size=(self.start_button_x,self.start_button_y),size_hint=(None, None),pos=(self.othello_board_x,self.start_button_y))
        self.add_widget(self.board,)
        
        self.add_widget(self.start_button)
        self.add_widget(self.text_widget)
        
        self.start_button.bind(on_press = self.start_faze)

        
        

    def on_touch_down(self, touch):
        pos = self.processing_pos(touch.pos)
        is_sandwitch = self.othello_board.judge_place(pos)
                
        
        if self.is_first_touch:
            self.is_first_touch=False
            
            if True in is_sandwitch:
                x,y = pos
                self.paint_circle.paint(list_pos=(x,y),turn=self.othello_board.turn)
                self.othello_board.board[y][x] = self.othello_board.turn
                self.othello_board.change_sandwitch(is_sandwitch,pos)
                for y in range(8):
                    for x in range(8):
                        if(self.othello_board.board[y][x]==self.othello_board.turn):
                            self.paint_circle.paint(list_pos=(x,y),turn=self.othello_board.board[y][x])
                is_sandwitch = []
                
                self.othello_board.turn_update()
                self.text_widget.print_turn(self.othello_board.turn)
            self.is_first_touch=True
           
                
            
        return super().on_touch_down(touch)
    

    
    def on_touch_up(self, touch):
        if not self.othello_board.judge_put_circle():
            self.othello_board.turn_update()
            self.text_widget.print_turn(self.othello_board.turn)
            self.is_first_touch=True
            if not self.othello_board.judge_put_circle():
                self.othello_board.winner=self.othello_board.judge_winner()
                self.text_widget.print_winner(self.othello_board.winner)
        pass
        

    def processing_pos(self,pos):
        x,y = pos
        
        pos_x = x//(self.othello_board_x/8)
        pos_y = y//(self.othello_board_y/8)
       
        return (int(pos_x),int(pos_y))
        

    def othello_start(self,):
        self.othello_board.board[::][::]=None
        
    def start_faze(self,instance):
        self.othello_board.start_faze()
        for y in range(8):
            for x in range(8):
                self.paint_circle.clear_circle(self.othello_board.board_pos[y][x])
        
        self.paint_circle.paint(list_pos=(3,3),turn = self.othello_board.board[3][3])
        self.paint_circle.paint(list_pos=(4,4),turn = self.othello_board.board[4][4])
        self.paint_circle.paint(list_pos=(3,4),turn = self.othello_board.board[3][4])
        self.paint_circle.paint(list_pos=(4,3),turn= self.othello_board.board[4][3])
    
        

        

