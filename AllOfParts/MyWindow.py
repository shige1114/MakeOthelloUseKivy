from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from AllOfParts.Widget.ImageWidget import ImageWidget
from AllOfParts.Widget.TextWidget import TextWidget
from AllOfParts.Model.BoardOfOthello import OthelloBoard
from AllOfParts.Paint.PaintOthello import PaintOthello
from kivy.core.window import Window
from AllOfParts.Paint.PaintCircle import PaintCircle
from ReversiCpu.Cpu import Cpu
import time
from ControllMV.MV import MV

class MyWindow(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.othello_board = OthelloBoard()
        self.othello_cpu = Cpu(turn=False)
        self.window_size = Window.size
        self.is_first_touch = True
        self.mv = MV()
        self.start = False
        self.othello_board_x = self.window_size[0]/3*2
        self.othello_board_y = self.window_size[1]
        self.cpu = False
        self.start_button_x = self.window_size[0]/3/2
        self.start_button_y = self.window_size[1]/3
        self.cpu_button_pos_x = self.othello_board_x+self.start_button_x
        self.text_widget_size=(self.window_size[0]/3,self.window_size[1]/3*2)
        self.is_puted = False
        self.board = PaintOthello(size = (self.othello_board_x,self.othello_board_y),pos=(0,0),window_size=self.window_size)
        self.paint_circle = PaintCircle(widget=self.board,widget_size=(self.othello_board_x,self.othello_board_y))
        self.start_button = Button(text="Start",size=(self.start_button_x,self.start_button_y),size_hint=(None, None), pos=(self.othello_board_x,0))
        self.text_widget = TextWidget(text="Start!",widget_size=self.text_widget_size,size=(self.start_button_x,self.start_button_y),size_hint=(None, None),pos=(self.othello_board_x,self.start_button_y))
        self.cpu_button = Button(text="CPU",size=(self.start_button_x,self.start_button_y),size_hint=(None, None), pos=(self.othello_board_x+self.start_button_x,0))
        #self.image_widget = ImageWidget(size=(self.start_button_x,self.start_button_y),size_hint=(None, None), pos=(self.othello_board_x,0))
        self.add_widget(self.board,)
        self.add_widget(self.cpu_button)
        self.add_widget(self.start_button)
        self.add_widget(self.text_widget)
        
        self.start_button.bind(on_press = self.start_faze)
        self.cpu_button.bind(on_press = self.cpu_action)
        
        

    def on_touch_down(self, touch):
        
        pos = self.processing_pos(touch.pos)
        is_sandwitch = self.othello_board.judge_place(pos)
                    
        
        if self.start:
                
            if True in is_sandwitch and not self.is_puted:
                self.mv.make_sound(turn=self.othello_board.turn)
                self.is_puted = True
                x,y = pos
                list_pos = self.othello_board.board_pos[y][x]     
               
                self.othello_board.board[y][x] = self.othello_board.turn
                self.othello_board.change_sandwitch(is_sandwitch,pos)
                self.paint_circle.board_update(board_pos=self.othello_board.board_pos,turn=self.othello_board.turn,board=self.othello_board.board)
                

                self.othello_board.turn_update()
                #self.text_widget.print_turn(self.othello_board.turn)
                self.is_first_touch=False

        return super().on_touch_down(touch)
    

    
    def on_touch_up(self, touch):
        x,y = touch.pos
        while True:
            if not self.othello_board.judge_put_circle():
                self.othello_board.turn_update()
                self.text_widget.print_turn(self.othello_board.turn)
                
                self.is_first_touch=True
                if not self.othello_board.judge_put_circle():
                    self.othello_board.winner=self.othello_board.judge_winner()
                    self.text_widget.print_winner(self.othello_board.winner)
                    return 0
            if not self.cpu:break
            if(self.othello_board.turn!=self.othello_cpu.turn):break
            if self.is_puted and self.othello_cpu.turn==self.othello_board.turn:
                if(x<self.othello_board_x and y<self.othello_board_y):self.cpu_faze()
        
        self.is_first_touch=True
        self.is_puted = False
        pass
        

    def processing_pos(self,pos):
        x,y = pos
        
        pos_x = x//(self.othello_board_x/8)
        pos_y = y//(self.othello_board_y/8)
       
        return (int(pos_x),int(pos_y))
        

    def othello_start(self,):
        self.othello_board.board[::][::]=None
        
    def start_faze(self,instance):
        self.start = not self.start
        self.othello_board.start_faze()
        for y in range(8):
            for x in range(8):
                self.paint_circle.clear_circle(self.othello_board.board_pos[y][x])
        
        self.paint_circle.paint(list_pos=self.othello_board.board_pos[3][3],turn = self.othello_board.board[3][3])
        self.paint_circle.paint(list_pos=self.othello_board.board_pos[4][4],turn = self.othello_board.board[4][4])
        self.paint_circle.paint(list_pos=self.othello_board.board_pos[3][4],turn = self.othello_board.board[3][4])
        self.paint_circle.paint(list_pos=self.othello_board.board_pos[4][3],turn= self.othello_board.board[4][3])
    
        
    def cpu_action(self,instance):

        self.cpu = not self.cpu

    def cpu_faze(self):
        start_time = time.time()
        if(self.cpu and self.start):
            
            if self.othello_board.remaining_moves>8:score,cpu_pos = self.othello_cpu.max_algha_bata_function(turn=self.othello_cpu.turn,board=self.othello_board.board,n=3,remaining_moves=self.othello_board.remaining_moves,start_time=start_time)
            else:score,cpu_pos = self.othello_cpu.max_algha_bata_function(turn=self.othello_cpu.turn,board=self.othello_board.board,n=self.othello_board.remaining_moves,remaining_moves=self.othello_board.remaining_moves,start_time=start_time)
            
            if type(cpu_pos)!=type(list()):return 0
            x,y = cpu_pos
            is_sandwitch = self.othello_board.judge_place(cpu_pos)
            self.othello_board.board[y][x] = self.othello_board.turn
            
            self.othello_board.change_sandwitch(is_sandwitch,cpu_pos)
            b = self.othello_board.board
            self.paint_circle.board_update(board_pos=self.othello_board.board_pos,turn=self.othello_board.turn,board=self.othello_board.board,)
            self.othello_board.turn_update()
            self.text_widget.print_turn(self.othello_board.turn)
        if not self.othello_board.judge_put_circle():
            self.othello_board.turn_update()
            self.text_widget.print_turn(self.othello_board.turn)
            self.is_first_touch=True
            if not self.othello_board.judge_put_circle():
                self.othello_board.winner=self.othello_board.judge_winner()
                self.text_widget.print_winner(self.othello_board.winner)

