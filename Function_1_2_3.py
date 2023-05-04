# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 21:17:31 2023

@author: zimoc
"""
#an empty list to store empty grids
all_grid_empty = []


def read_file(file_name):
    '''
    This function is using to read file with one grid and return a list which store the grides
    '''
    #read and return the grid which will be used in solving
    with open(file_name, 'r') as file:
        
        lines = file.readlines()

    grid = [[int(num) for num in line.strip().split(',')] for line in lines]
    
    #safe the grid which is empty and will be used to show hints
    with open(file_name, 'r') as file:
        
        lines = file.readlines()

    grid_empty = [[int(num) for num in line.strip().split(',')] for line in lines]
    
    all_grid_empty.append(grid_empty)
    
    return grid
    

def safe_file(name,suduku):
    '''
    This function safe each socution saperately as a txt, file
    '''
    #chage the final number with number and discription
    name = 'grid ' + name + ' solution in square.txt'
    
    with open(name, 'w') as output_file:
        # Write the original lines to the output file
        for original_line in suduku:
            
            output_file.write(' '.join(map(str, original_line)) + '\n')




def get_all_list_sep(main_list):
    
    '''
    this functin is to deal with the all hints which get from main, seperate them to as the order of gards 
    '''
    global all_list_sep
    all_list_sep = [[]]
    list_sep_num = 0
    list_mumber = 0
    
    #creat a list to sort all hints for each greads separeately. Also determing graids number.
    for item in main_list:
        #seperate the hints by ['+++++++'] which is used to distinguish hints for different grads
        if item == ['+++++++']:
            
            list_mumber += 1
            all_list_sep.append([])
            
    #store the hints in the list we have creat      
    for item in main_list:
        
        if item == ['+++++++']:
            
            list_sep_num += 1

        else:
            all_list_sep[list_sep_num].append(item)
    
    #formular hits
    for list_n in range(len(all_list_sep)-1):
        
        all_list_sep[list_n+1] = all_list_sep[list_n+1][len(all_list_sep[list_n]):]
        
    del all_list_sep[-1]
    
    return all_list_sep
            


def show_hints(main_list,hint_number):
    '''
    this function is used to show number of hints needed, and fill the original grids with the number if hits and print the grids out 
    '''
    
    all_list_sep = get_all_list_sep(main_list)   
    
    
    for each_list in range(len(all_list_sep)):
        
        if hint_number != 0:  
            
            #print grides number
            print('')
            print(hint_number,"hints for grid",each_list+1)
            
        for hints_ in range(hint_number):
            
            try:
                
                #print the number of hints and fill the blank
                print('hint',hints_+1,':')
                all_grid_empty[each_list][all_list_sep[each_list][hints_][1]-1][all_list_sep[each_list][hints_][2]-1] = all_list_sep[each_list][hints_][0]
                print(f'Put {all_list_sep[each_list][hints_][0]} in location {all_list_sep[each_list][hints_][1],all_list_sep[each_list][hints_][2]}')
                
            except:
                
                # if the number of hint is out of the range of blank we print a message
                print("no more hints")  
                
                break
            
        if hint_number != 0:  
            
            #print the original grid with hints
            print('\noriginal grid with hints:')
            print(all_grid_empty[each_list])
        
                
def store_all_hints(name):
    '''
    This fintion is used to to store the solution in text seperately
    '''
    #find solution for each gieds in the list we have processed
    for each_grids in range(len(all_list_sep)):
        
        #store the selution in text
        with open(name, 'a+') as file:
            
            file.write(f'grid number: {each_grids+1}\n')
            hits_number_for_print = 1
            
            for item in all_list_sep[each_grids]:
                
                file.write(f'hints number: {hits_number_for_print}\n')
                hits_number_for_print += 1
                file.write(f'Put {item[0]} in location {item[1],item[2]}\n')
    

def print_all_hints():
    '''
    This function is used to print all the solution for all grides in the terminal
    '''
    #find solution for each gieds in the list we have processed
    for each_grids in range(len(all_list_sep)):
        
        print('\n==============================')
        print(f"Solution in text for {each_grids+1}\n" )
        hits_number_for_print = 1
        
        #print the hints
        for item in all_list_sep[each_grids]:
            print(f'hints number: {hits_number_for_print}')
            hits_number_for_print += 1
            print(f'Put {item[0]} in location {item[1],item[2]}')
