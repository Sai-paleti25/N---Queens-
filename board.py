# -*- coding: utf-8 -*-
"""
Created on thursday March 26  2020

@authors: Aditya Kadimi,
          Mrudula Ravipati ,
          Sai Harish Paleti.
"""

import numpy as np

class Queen:
    
    def __init__(self,r,c):  
        self.r=r
        self.c=c
        
    def attack_check(self,q):
        return  self.r ==q.get_rows() or self.c==q.get_columns() or abs(self.c - q.get_columns()) == abs(self.r - q.get_rows())
    
    def go_down(self,steps):
        self.r = (self.r + steps) % Board.get_size();
        
    def get_rows(self):
        return self.r
    
    def get_columns(self):
        return self.c
    
    def toString(self):
        return "(" + str(self.r) + ", " + str(self.c) + ")"
    
class Board:
    board_size=8

    def __init__(self):  
        self.state=[]
        self.next_board=[]
        self.h=0
        
    def Board(self,n):  
        for i in range(Board.board_size):
            self.state.append(Queen(n.state[i].get_rows(), n.state[i].get_columns()))
    
    
    def get_size():
        return Board.board_size
    
    def set_size(size):
        Board.board_size=size
        
    def create_board(self, initial_state):
        count=0
        for i in range(Board.board_size):
            for j in range(1,Board.board_size):
                new_board=Board()
                new_board.Board(initial_state)
                self.next_board.insert(count, new_board )
                self.next_board[count].state[i].go_down(j)
                self.next_board[count].calculate_h()
                count+=1
    
        return self.next_board
    
    def calculate_h(self):
        for i in range(Board.board_size-1):
            for j in range(i+1,Board.board_size):
                if (self.state[i].attack_check(self.state[j])):
                    self.h+=1
        return self.h
    
    def get_h(self):
        return self.h
    
    def compare(self,n):
        if(self.h<n.get_h()):
            return -1
        elif(self.h>n.get_h()):
            return 1
        else:
            return 0
    
    def set_state_board(self,s):
        for i in range(Board.board_size):
            self.state.append( Queen(s[i].get_rows(), s[i].get_columns()))
        
    def toString(self):
        result=""
        board = np.zeros((Board.get_size(),Board.get_size()), dtype=str)
        for i in range(Board.board_size):
            for j in range(Board.board_size):
                board[i][j]="#"
        for i in range(Board.board_size):
            board[self.state[i].get_rows()][self.state[i].get_columns()]="Q"
        for i in range(Board.board_size):
            for j in range(Board.board_size):
                result+=board[i][j]
            result += "\n"
        return result