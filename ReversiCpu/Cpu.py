#!/usr/bin/pyenv python
# # -*- coding: utf-8 -*-
__author__ = "HAMAGUCHI SHIGENAGA"
__date__ = 2022/3/6
__ver__ = "0.0.0"
from copy import deepcopy
from math import trunc
from sysconfig import is_python_build
import time
from turtle import shape, shapesize
from AllOfParts.Model.BoardOfOthello import OthelloBoard
ESCAPE_TIME = 000.4
REMAINING_MOVES = 6
RIMIT_SVM = 4
class Cpu:
   
    class ValueToRecordScore:
        def __init__(self) -> None:
            self.all_score = 0
            self.pos_score = 0
            self.shape_score = 0
            self.first_blood=10
            pass
        def total_score(self):
            
            pass
        
    def __init__(self,turn) -> None:
        self.othello_board = OthelloBoard()
        self.turn = turn
        self.vec = [[0,1],[1,0],[1,1],[-1,0],[0,-1],[-1,-1],[1,-1],[-1,1]]
        pass

    def static_merit_function(self,**args):
        """
        {args board,num,}
        {return score,}
        """

        
        my_score = self.ValueToRecordScore()
        oppo_score = self.ValueToRecordScore()

        shape_score = 30
        score_of_board = [
            [120,-20,20,5,5,20,-20,120],
            [-20,-30,-5,-5,-5,-5,-30,-20],
            [20,-5,15,3,3,15,-5,20],
            [5,-5,3,3,3,3,-5,5],
            [5,-5,3,3,3,3,-5,5],
            [20,-5,15,3,3,15,-5,20],
            [-20,-30,-5,-5,-5,-5,-30,-20],
            [120,-20,20,5,5,20,-20,120],
            ]
        courners = [[7,7],[0,0],[0,7],[7,0]]
        args["dif_turn"]= not self.turn

        for y in range(8):
            for x in range(8):
                if(args["board"][y][x]==None):continue
                if args["board"][y][x] == self.turn:my_score.pos_score+=score_of_board[y][x]
                if args["board"][y][x] != self.turn:oppo_score.pos_score += score_of_board[y][x]

        for couner in courners:
            x,y = couner
            for vec in self.vec:
                mv_x,mv_y = x,y
                for _ in range(3):
                    mv_x+=vec[0]
                    mv_y+=vec[1]
                    if(mv_x>=0 and mv_x<8):
                        if(mv_y>=0 and mv_y<8):
                            if(args["board"][mv_y][mv_x]!=self.turn):break
                else:oppo_score.shape_score+=shape_score
        for couner in courners:
            x,y = couner
            for vec in self.vec:
                mv_x,mv_y = x,y
                for _ in range(3):
                    mv_x+=vec[0]
                    mv_y+=vec[1]
                    if(mv_x>=0 and mv_x<8):
                        if(mv_y>=0 and mv_y<8):
                            if(args["board"][mv_y][mv_x]!= args["dif_turn"]):break
                else:my_score.shape_score+=shape_score
                
        put_pos_inf = self.all_put_pos(board=args["board"],turn=args["turn"])
        if put_pos_inf["num"]!=None:my_score.all_score = 0.6*my_score.pos_score + 0.1*put_pos_inf["num"] + my_score.shape_score*0.4
        else:my_score.all_score = 0.6*my_score.pos_score + my_score.shape_score*0.4
        put_pos_inf = self.all_put_pos(board=args["board"],turn=not args["turn"])
        if put_pos_inf["num"]!=None:oppo_score.all_score = 0.6*oppo_score.pos_score + 0.1*put_pos_inf["num"] + oppo_score.shape_score*0.4
        else:oppo_score.all_score = 0.6*oppo_score.pos_score + oppo_score.shape_score*0.4
        
        return my_score.all_score-oppo_score.all_score
        pass

    def maximize_number_function(self,**args):

        score = 0
        num = 0
        
        for y in range(8):
            for x in range(8):
                if args["board"][y][x]==self.turn:num+=1
        
        put_pos_inf = self.all_put_pos(board=args["board"],turn=not self.turn)
        if put_pos_inf["num"]!=None:score -= 0.5*put_pos_inf["num"]

        score += num
        return score

        pass

    def max_algha_bata_function(self,turn,n=3,board=None,algha = None,remaining_moves=None,start_time = None):
        end_time = 0
        global ESCAPE_TIME
        if remaining_moves<=REMAINING_MOVES:ESCAPE_TIME=0.3
        if(n==0 or end_time-start_time>=ESCAPE_TIME):
            if(remaining_moves>=REMAINING_MOVES):return self.static_merit_function(board=board,turn = turn),0,
            else:return self.maximize_number_function(board=board,turn = turn),0,
        
        c_board = deepcopy(board)
        inf_of_put = self.all_put_pos(board=c_board,turn=turn)
        best_pos = None
        max_score = None
        can_pos = inf_of_put["can_put"]
        all_pos = inf_of_put["put_poss"]
        score = 0
        max_score = -99999999999
        if(not inf_of_put["is_put"]):return self.static_merit_function(board=board,turn = turn),0
        for cp_y in range(len(can_pos)):
            for cp_x in range(len(can_pos[cp_y])):
                if can_pos[cp_y][cp_x]:
                    
                    sanded_board=self.change_sand(c_board,all_pos[cp_y][cp_x],pos=[cp_x,cp_y],turn=turn)
                    if n>=RIMIT_SVM:
                        start_time=time.time()
                        
                    score,p,= self.min_algha_bata_function(n=n-1,turn=not turn,board=sanded_board,beta=max_score,remaining_moves=remaining_moves,start_time=start_time)
                 
                    """
                      if algha!=None:
                        if algha<score:
                            return algha,0
                    """
                  
                    
                    
                    
                    
                    if(score>max_score):
                        best_pos = [cp_x,cp_y]
                        max_score=score
                        print(score)
        
                    
        return max_score,best_pos,
        pass

    def min_algha_bata_function(self,turn,n=3,board=None,beta=None,remaining_moves=None,start_time = None):
        
        end_time = 0
        if(n==0 or end_time-start_time>=ESCAPE_TIME):
            
            if(remaining_moves<=REMAINING_MOVES):return self.static_merit_function(board=board,turn = turn),0,
            else:return self.maximize_number_function(board=board,turn = turn),0,
        c_board = deepcopy(board)
        inf_of_put = self.all_put_pos(board=c_board,turn=turn)
        min_pos = None
        can_pos = inf_of_put["can_put"]
        all_pos = inf_of_put["put_poss"]
        score = 0
        min_score = 999999999989
        if(not inf_of_put["is_put"]):return self.static_merit_function(board=board,turn = turn),0
        for cp_y in range(len(can_pos)):
            for cp_x in range(len(can_pos[cp_y])):
                if not can_pos[cp_y][cp_x]:continue
                start_time = time.time()
                sanded_board=self.change_sand(c_board,all_pos[cp_y][cp_x],pos=[cp_x,cp_y],turn=turn)
                score,p, = self.max_algha_bata_function(n=n-1,turn=not turn,board=sanded_board,algha=min_score,remaining_moves=remaining_moves,start_time=start_time)
                if n>=RIMIT_SVM:start_time=time.time()
                
                """
                if beta!=None:
                    if beta>score:
                        return beta,0
                """
                

                
                if(score<min_score):
                    min_score=score
                    min_pos=[cp_x,cp_y]
                    print(score)
        return min_score,min_pos,
        pass

    def all_put_pos(self,turn,board):
        """
        {args can_put,put_poss,is_put,sand,num}
        {return re_value}
        """
        can_put = [[None for _ in range(8)]for _ in range(8)]
        put_poss = [[[] for _ in range(8)]for _ in range(8)]
        mv_vecs = self.vec
        is_put = False
        re_value = dict()
        re_value["num"]=0
        for mv_v in mv_vecs:
            for y in range(8):
                for x in range(8):
                    
                    args=self.mvn(num=0,board=board,vec=mv_v,turn=turn,pos=[x,y],sand=False)
                    if  can_put[y][x]!=True:
                        can_put[y][x]=args["sand"]

                    if args["sand"]:
                        re_value["num"]+=1
                        is_put = True
                        put_poss[y][x].append(args["num"])
                    else:put_poss[y][x].append(0)
        re_value["can_put"]=can_put
        re_value["put_poss"]=put_poss
        re_value["is_put"]=is_put
        return re_value
        pass

    def mvn(self,**args):
        x,y = args["pos"]
        board = args["board"]
        if(args["num"]==0 and args["board"][y][x]!=None):return args
        x+=args["vec"][0]
        y+=args["vec"][1]
        
        if(x>=0 and x<8):
            if(y>=0 and y<8):

                if(board[y][x]==args["turn"]):
                    if(args["num"]>0):
                        args["sand"]=True
                        return args

                elif(board[y][x]!=None):
                    args["num"]+=1
                    args["pos"]=[x,y]
                    return self.mvn(**args)
                
                
        
        return args
        pass
    
    def change_sand(self,board,put_pos,pos,turn):
        cp_board = deepcopy(board)
        cp_board[pos[1]][pos[0]] = turn
        for vec in self.vec:
            for _ in range(put_pos[self.vec.index(vec)]):
                cp_board[pos[1]+vec[1]][pos[0]+vec[0]]=turn
        return cp_board
        pass