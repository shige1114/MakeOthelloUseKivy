#!/usr/bin/pyenv python
# # -*- coding: utf-8 -*-
__author__ = "HAMAGUCHI SHIGENAGA"
__date__ = 2022/3/6
__ver__ = "0.0.0"
from copy import deepcopy
from sysconfig import is_python_build
from time import sleep
from AllOfParts.Model.BoardOfOthello import OthelloBoard
class Cpu:

    def __init__(self,turn) -> None:
        self.othello_board = OthelloBoard()
        self.turn = turn
        self.vec = [[0,1],[1,0],[1,1],[-1,0],[0,-1],[-1,-1],[1,-1],[-1,1]]
        pass

    def static_merit_function(self,**args):
        score=0
        score_of_board = [
            [120,-20,20,5,5,20,-20,120],
            [-20,-40,-5,-5,-5,-5,-40,-20],
            [20,-5,15,3,3,15,-5,20],
            [5,-5,3,3,3,3,-5,5],
            [120,-20,20,5,5,20,-20,120],
            [-20,-40,-5,-5,-5,-5,-40,-20],
            [20,-5,15,3,3,15,-5,20],
            [5,-5,3,3,3,3,-5,5],
            ]
        courners = [[7,7],[0,0],[0,7],[7,0]]
        for couner in courners:
            x,y = couner
            if(args["board"][y][x]!=args["turn"]):continue
            else:score+=score_of_board[y][x]
            for vec in self.vec:
                mv_x,mv_y = x,y
                for _ in range(3):
                    
                    mv_x+=vec[0]
                    mv_y+=vec[1]
                    if(mv_x>=0 and mv_x<8):
                        if(mv_y>=0 and mv_y<8):
                            if(args["board"][mv_y][mv_x]!=args["turn"]):break
                        

                else:score+=10
        put_pos_inf = self.all_put_pos(board=args["board"],turn=args["turn"])
        if put_pos_inf["num"]!=None:score += score+0.1*put_pos_inf["num"]
        return score
        pass

    def max_algha_bata_function(self,turn,n=3,board=None,):
        if(n==0):return self.static_merit_function(board=board,turn = turn),0
        c_board = deepcopy(board)
        inf_of_put = self.all_put_pos(board=c_board,turn=turn)
        best_pos = None
        max_score = None
        can_pos = inf_of_put["can_put"]
        all_pos = inf_of_put["put_poss"]
        score = 0
        max_score = 0
        if(not inf_of_put["is_put"]):return self.static_merit_function(board=board,turn = turn),0
        for cp_y in range(len(can_pos)):
            for cp_x in range(len(can_pos[cp_y])):
                if can_pos[cp_y][cp_x]:
                    
                    sanded_board=self.change_sand(c_board,all_pos[cp_y][cp_x],pos=[cp_x,cp_y],turn=turn)
                    score,p = self.min_algha_bata_function(n=n-1,turn=not turn,board=sanded_board)

                    
                    if(score>max_score):
                        best_pos = [cp_x,cp_y]
                        max_score=score
                    
        return max_score,best_pos
        pass

    def min_algha_bata_function(self,turn,n=3,board=None,):
        if(n==0):return self.static_merit_function(board=board,turn = turn),0
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
                
                sanded_board=self.change_sand(c_board,all_pos[cp_y][cp_x],pos=[cp_x,cp_y],turn=turn)
                score,p = self.max_algha_bata_function(n=n-1,turn=not turn,board=sanded_board)

                if(score!=None):
                    if(score<min_score):
                        min_score=score
                        min_pos=[cp_x,cp_y]

        return min_score,min_pos
        pass

    def all_put_pos(self,turn,board):
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
        board[pos[1]][pos[0]] = turn
        for vec in self.vec:
            for _ in range(put_pos[self.vec.index(vec)]):
                board[pos[1]+vec[1]][pos[0]+vec[0]]=turn
        return board
        pass