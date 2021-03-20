# -*- coding: utf-8 -*-
"""
Created on thursday March 26  2020

@authors: Aditya Kadimi,
          Mrudula Ravipati ,
          Sai Harish Paleti.
"""

import random
from board import Board
from board import Queen
from Steepest_Ascent import Steepest_Ascent

class Random_Restart_Steepest_Ascent:
    
    
    def __init__(self,s):  
        self.step=0
        self.start=0
        self.steepest_ascent_obj= Steepest_Ascent(s)
        Random_Restart_Steepest_Ascent.restart_used=1
        
    def climbing_algorithm(self,s):
        curr_board=self.steepest_ascent_obj.get_start_board()
        self.set_start_board(curr_board)
        h= curr_board.get_h()
        self.step=0
        
        while h!=0:
            next_board= self.steepest_ascent_obj.climbing_algorithm()
            self.step+= self.steepest_ascent_obj.get_steps()
            h = next_board.get_h()
        
            if h!=0:
                s=Random_Restart_Steepest_Ascent.generate_board()
                self.steepest_ascent_obj= Steepest_Ascent(s)
                Random_Restart_Steepest_Ascent.restart_used+=1
            else:
                curr_board=next_board
                self.step-= self.steepest_ascent_obj.get_steps()
                Random_Restart_Steepest_Ascent.restart_used+=1
        return curr_board
    
    
    def generate_board():
        start=[]
        for i in range(8):
            start.append( Queen(random.randint(0,Board.get_size()-1) ,i))
        return start
    def set_start_board(self, curr_board):
        self.start = curr_board
    def get_step_count(self):
        return self.step
    def get_random_used(self):
        return Random_Restart_Steepest_Ascent.restart_used