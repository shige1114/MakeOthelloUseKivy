from curses.ascii import ispunct
from kivy.core.window import Window
from AllOfParts.Model.Player import Player

class OthelloBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)]for _ in range(8)]        
        self.board[4][4] = True
        self.board[3][3] = True
        self.board[4][3] = False
        self.board[3][4] = False
        self.player_1 = Player(True)
        self.player_2 = Player(False)
        self.turn = True

        self.winner = None
        
        self.size = Window.size
        self.Othello_x = self.size[0]/3*2
        self.Othello_y = self.size[1]

        self.board_pos = [[() for _ in range(8)]for _ in range(8)]
        self.board_pos = self.make_board_pos(self.board_pos)
        self.move_vec = [(0,1),(1,0),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]


    def turn_update(self):
        if(self.turn):self.turn=False
        else:self.turn=True

    def make_board_pos(self,pos_list):
        a_mas_x=self.Othello_x/8+0.5
        a_mas_y=self.Othello_y/8+0.5
        for y in range(8):
            for x in range(8):
                pos_list[y][x] = (a_mas_x*x,a_mas_y*y)
        return pos_list

    def judge_place(self,pos):
        x,y = pos
        is_first = True
        is_sandwitch = []

        if(len(self.board)>y and y>=0):
            if(len(self.board)>x and x>=0):
                if(self.board[y][x]==None):    
                    for vec in self.move_vec:
                        if self.mvn(x,y,vec,is_first):is_sandwitch.append(True)
                        else:is_sandwitch.append(False)
        
        return is_sandwitch

    def change_sandwitch(self,is_sandwitch,pos):
         
        for i in range(len(is_sandwitch)):
            if(is_sandwitch[i]):
                x,y = pos
                vec_x,vec_y = self.move_vec[i]
                while True:
                    y+=vec_y
                    x+=vec_x
                    if(self.board[y][x]==None):break
                    if(self.board[y][x]==self.turn):break
                    self.board[y][x]=self.turn
        pass
                    
                 
    def judge_put_circle(self):
        is_put = []
        for y in range(8):
            for x in range(8):
                is_put = self.judge_place((x,y))
                if True in is_put:return True
        
        return False
            
    def judge_winner(self):

        for y in range(8):
            for x in range(8):
                if self.player_1.turn == self.board[y][x]:self.player_1.num_circle+=1
                elif self.player_2.turn == self.board[y][x]:self.player_2.num_circle+=1

        if(self.player_1.num_circle>self.player_2.num_circle):return self.player_1.turn
        else:return self.player_2.turn

    def start_faze(self):
        self.board = [[None for _ in range(8)]for _ in range(8)]        
        self.board[4][4] = True
        self.board[3][3] = True
        self.board[4][3] = False
        self.board[3][4] = False
        self.player_1 = Player(True)
        self.player_2 = Player(False)
        self.turn = True
        self.winner = None


    def mvn(self,x,y,vec,is_first):
        vec_x,vec_y = vec
        
        if(len(self.board)>y+vec_y and 0<=y+vec_y):
            if(len(self.board[y])>x+vec_x and 0<=x+vec_x):
                
                if(self.turn == self.board[y+vec_y][x+vec_x]):
                    
                    if(is_first==False):return True
                    else:return False

                elif(self.board[y+vec_y][x+vec_x]!=self.turn and self.board[y+vec_y][x+vec_x]!=None):
                    return self.mvn(x+vec_x,y+vec_y,vec,is_first=False)

                else:return False
            return False
        return False

