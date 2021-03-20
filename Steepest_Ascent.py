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

class Steepest_Ascent:
    
    
    
    def __init__(self,s):  
        self.step=0
        self.print_nodes=[]
        self.start_board= Board()
        start_state= []
        for i in range(Board.get_size()):
            start_state.append((Queen(s[i].get_rows(),s[i].get_columns())))
        self.start_board.set_state_board(start_state)
        self.start_board.calculate_h()
    

    
    def climbing_algorithm(self):
        curr_board=self.start_board
        
        while True:
            successors=curr_board.create_board(curr_board)
            exist_better = False
            self.print_nodes.append(curr_board)
            self.step+=1
            
            for i in range(len(successors)):
                if(successors[i].compare(curr_board) < 0):
                    curr_board=successors[i]
                    exist_better=True
                    
            if not exist_better:
                return curr_board
    def list_to_print(self):
        return self.print_nodes
    
    def print_path(self,print_nodes):
        for i in range(len(self.print_nodes)):
            print(self.print_nodes[i].toString())
    
    def get_start_board(self):
        return self.start_board
    
    def get_steps(self):
        return self.step
        