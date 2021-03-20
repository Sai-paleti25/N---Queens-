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

class Sideways_Move:
    
    def __init__(self,s):
        first_state=[]
        self.initial=Board()
        self.step=0
        self.print_node=[]
        for i in range(Board.get_size()):
            first_state.append((Queen(s[i].get_rows(),s[i].get_columns())))
        self.initial.set_state_board(first_state)
        self.initial.calculate_h()
        
    def climbing_algorithm(self):
        current_board=self.initial
        count=0
        
        while True:
            successors=current_board.create_board(current_board)
            select_random_successors=[]
            
            exist_better =False;
            exist_best=False
            
            self.print_node.append(current_board)
            
            for i in range(len(successors)):
                if count==100:
                    break
                if(successors[i].compare(current_board) <= 0):
                    if(successors[i].compare(current_board) < 0):
                        count=0
                        select_random_successors=[]
                        current_board=successors[i]
                        exist_better=True
                        self.step+=1
                    elif(successors[i].compare(current_board) == 0):
                        select_random_successors.append(successors[i])
                        
            if not exist_better and not not select_random_successors:
                
                current_board= select_random_successors[random.randint(0,len(select_random_successors))-1]
                exist_best=True
                count +=1
                self.step+=1
            if not exist_best and not exist_better:
                
                return current_board
            
    def get_start_board(self):
        return self.initial
    
    def print_path(self,print_nodes):
        for i in range(len(self.print_node)):
            print(self.print_node[i].toString())
            
    def list_to_print(self):
        return self.print_node
    
    def get_step_count(self):
        return self.step