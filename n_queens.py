# -*- coding: utf-8 -*-
"""
Created on thursday March 26  2020

@authors: Aditya Kadimi, Mrudula Ravipati , Sai Harish Paleti.
"""

import numpy as np
import random
from board import Board
from board import Queen
from Steepest_Ascent import Steepest_Ascent
from Sideways_Move import Sideways_Move
from Random_Restart_Steepest_Ascent import Random_Restart_Steepest_Ascent
from Random_Restart_Sideways import Random_Restart_Sideways

board_size = input("Enter the the value for number of queens in n-Queen problem: ")
board_size=int(board_size)
runtime = input("Please enter the Runtime: ")
runtime=int(runtime)


Board.set_size(board_size)




def generate_board():
    start=[]
    for i in range(board_size):
        start.append( Queen(random.randint(0,board_size-1) ,i))
    return start

steepest_ascent_sum_succes=0
steepest_ascent_aver_success=0
steepest_ascent_success_steps=0
steepest_ascent_aver_succes_steps=0
steepest_ascent_faill_steps=0
steepest_ascent_aver_faiil_steps=0

side_move_sum_succes=0
side_move_aver_succes=0
side_move_aver_succes=0
side_move_aver_succes_steps=0
side_move_fail_steps=0
side_move_aver_fail_steps=0

random_restart_steepest_ascent_summ_succes=0
random_restart_steepest_ascent_aver_succes=0
random_restart_steepest_ascent_succes_steps=0
random_restart_steepest_ascent_aver_succes_steps=0
random_restart_steepest_ascent_count=0

random_restart_side_move_sum_succes=0
random_restart_side_move_aver_succes=0
random_restart_side_move_aver_succes=0
random_restart_side_move_aver_succes_steps=0
random_restart_side_moves_count=0



for current_test in range(1,runtime+1):
    initial_board= generate_board()
    
    steepest_ascent= Steepest_Ascent(initial_board)
    random_restart_steepest_ascent = Random_Restart_Steepest_Ascent(initial_board)
    sideways_move= Sideways_Move(initial_board)
    random_restart_sideways_move= Random_Restart_Sideways(initial_board)
    
    steepest_ascent_board= steepest_ascent.climbing_algorithm()
    random_restart_steepest_ascent_board = random_restart_steepest_ascent.climbing_algorithm(initial_board)
    sideways_move_board= sideways_move.climbing_algorithm()
    random_restart_sideways_move_board= random_restart_sideways_move.climbing_algorithm(initial_board)
    
    #steepest Ascent
    
    if steepest_ascent_board.calculate_h()==0:
        steepest_ascent_sum_succes+=1
        steepest_ascent_success_steps= steepest_ascent.get_steps()
        steepest_ascent_aver_succes_steps+=steepest_ascent_success_steps
        
    else:
        steepest_ascent_faill_steps=steepest_ascent.get_steps()
        steepest_ascent_aver_faiil_steps += steepest_ascent_faill_steps


    if current_test==33:
        print("First Path for Steepest Ascent")
        x = steepest_ascent.list_to_print()
        steepest_ascent.print_path(x)
        print("Path cost: ", len(x))

    if current_test==97:
        print("Second Path for Steepest Ascent")
        x = steepest_ascent.list_to_print()
        steepest_ascent.print_path(x)
        print("Path cost: ", len(x))
        
    if current_test==139:
        print("Third Path for Steepest Ascent")
        x = steepest_ascent.list_to_print()
        steepest_ascent.print_path(x)
        print("Path cost: ",len(x))
        
    #Random Restart Steepest Ascent
    
    if random_restart_steepest_ascent_board.get_h() == 0 :
        random_restart_steepest_ascent_summ_succes+=1

        random_restart_steepest_ascent_succes_steps=random_restart_steepest_ascent.get_step_count()
        random_restart_steepest_ascent_aver_succes_steps+=random_restart_steepest_ascent_succes_steps
        random_restart_steepest_ascent_count+=random_restart_steepest_ascent.get_random_used()
                
    #Sideways move
    if sideways_move_board.get_h() == 0:
        side_move_sum_succes+=1
        side_move_aver_succes=sideways_move.get_step_count()
        side_move_aver_succes_steps+=side_move_aver_succes

    else:
        side_move_fail_steps=sideways_move.get_step_count()
        side_move_aver_fail_steps+=side_move_fail_steps
        
    if current_test==181:
        print("First Path for Steepest Ascent Sideways Move")
        x = sideways_move.list_to_print()
        sideways_move.print_path(x)
        print("Path cost: ",len(x))
    if current_test==214:
        print("Second Path for Sideways Move")
        x = sideways_move.list_to_print()
        sideways_move.print_path(x)
        print("Path cost: ",len(x))

    if current_test==376:
        print("Third Path for Sideways Move")
        x = sideways_move.list_to_print()
        sideways_move.print_path(x)
        print("Path cost: ",len(x))
        
    #Random Restart without sideways move
    if random_restart_sideways_move_board.get_h() == 0:
        random_restart_side_move_sum_succes+=1
        random_restart_side_move_aver_succes=random_restart_sideways_move.get_step_count()
        random_restart_side_move_aver_succes_steps+= random_restart_side_move_aver_succes;
        random_restart_side_moves_count+=(random_restart_sideways_move.get_random_used());
                
                
steepest_ascent_aver_success=steepest_ascent_sum_succes/runtime
random_restart_steepest_ascent_aver_succes = random_restart_steepest_ascent_summ_succes / runtime;
side_move_aver_succes= side_move_sum_succes/ runtime
random_restart_side_move_aver_succes =random_restart_side_move_sum_succes / runtime;


print("Steepest Ascent :"

                    + " Success Count = " , steepest_ascent_sum_succes
                    , " Success rate = " , steepest_ascent_aver_success
                    , " Fail count = " , (runtime - steepest_ascent_sum_succes)
                    , " Failure rate = " , (1 - steepest_ascent_aver_success)
                    , " Avg Success Steps = " , (steepest_ascent_aver_succes_steps/steepest_ascent_sum_succes)
                    , " Avg Fail Steps : " , ((steepest_ascent_aver_faiil_steps)/(runtime-steepest_ascent_sum_succes)));


print("Random Restart Steepest Ascent:"

                    , " Success Count = " , random_restart_steepest_ascent_summ_succes
                    , " Success rate = " , random_restart_steepest_ascent_aver_succes
                    , " Fail Count = " , (runtime - random_restart_steepest_ascent_summ_succes)
                    , " Failure rate = " , (1 - random_restart_steepest_ascent_aver_succes)
                    , " Avg Success Steps = " , ((random_restart_steepest_ascent_aver_succes_steps)/runtime)
                    , " Avg Random Restart =" , (random_restart_steepest_ascent_count/runtime));

print("Sideways Move :"

                    , " Success Count = " , side_move_sum_succes
                    , " Success rate = " , side_move_aver_succes
                    , " Fail count  = " , (runtime - side_move_sum_succes)
                    , " Failure rate = " , (1 - side_move_aver_succes)
                    , " Avg Success Steps = " , (side_move_aver_succes/side_move_sum_succes)
                    , " Avg Fail Steps = " , (np.float64(side_move_aver_fail_steps)/(runtime-side_move_sum_succes)));

print("Random Restart Sideways :"

                , " Success Count = " , random_restart_side_move_sum_succes
                , " Success rate = " , random_restart_side_move_aver_succes
                , " Fail Count = " , (runtime - random_restart_side_move_sum_succes)
                , " Failure rate = " , (1 - random_restart_side_move_aver_succes)
                , " Avg Success Steps = " , ((random_restart_side_move_aver_succes_steps)/runtime)
                , " Avg Random Restart = " , (random_restart_side_moves_count)/runtime);

        