# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 21:17:31 2023

@author: zimoc
"""

all_grid_empty = []

def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    grid = [[int(num) for num in line.strip().split(',')] for line in lines]

    #print(grid)
    
    with open(file_name, 'r') as file:
        
        lines = file.readlines()

    grid_empty = [[int(num) for num in line.strip().split(',')] for line in lines]

    #print(grid)
    all_grid_empty.append(grid_empty)
    
    
    return grid
    

def safe_file(name,suduku):
    with open(name, 'w') as output_file:
        # Write the original lines to the output file
        for original_line in suduku:
            output_file.write(' '.join(map(str, original_line)) + '\n')




def get_all_list_sep(main_list):
    
    global all_list_sep
    all_list_sep = [[]]
    list_sep_num = 0
    list_mumber = 0
    #single_list_number_for_one_grid = 0
    
    #creat a list to sort all hints for each greads separeately. Also determing graids number.
    for item in main_list:
        if item == ['+++++++']:
            list_mumber += 1
            all_list_sep.append([])
    #print('all_list_sep',all_list_sep)
    #print('all_list_sep[list_sep_num] =',all_list_sep[list_sep_num])
    
    #store hints
    for item in main_list:
        
        if item == ['+++++++']:
            #print( list_sep_num )
            list_sep_num += 1
            #single_list_number_for_one_grid = 0

        
        else:
            all_list_sep[list_sep_num].append(item)
            #single_list_number_for_one_grid += 1
        
   
    
    #formular hits
    for list_n in range(len(all_list_sep)-1):
        all_list_sep[list_n+1] = all_list_sep[list_n+1][len(all_list_sep[list_n]):]
    del all_list_sep[-1]
    
    return all_list_sep
            


def show_hints(main_list,hint_number):
    all_list_sep = get_all_list_sep(main_list)
    
    
    #print('len(all_list_sep)',len(all_list_sep))
    
    for each_list in range(len(all_list_sep)):
        print('')
        print("hints for grid",each_list+1)
        for hints_ in range(hint_number):
            try:
                print('hint',hints_+1,':')
                #print(all_list_sep[each_list][hints_])
            
                #print(all_list_sep[each_list][hints_][1])
                #print(all_list_sep[each_list][hints_][2])
                #print(all_list_sep[each_list][hints_][0])
            
                #print(all_grid_empty[each_list])
                all_grid_empty[each_list][all_list_sep[each_list][hints_][1]-1][all_list_sep[each_list][hints_][2]-1] = all_list_sep[each_list][hints_][0]
                print(f'Put {all_list_sep[each_list][hints_][0]} in location {all_list_sep[each_list][hints_][1],all_list_sep[each_list][hints_][2]}')
            except:
                print("no more hints")  #print(all_grid_empty[each_list])
                break
            
        print('blank grid with hints:')
        print(all_grid_empty[each_list])
        
'''        
def show_all_hints():
    print("")
    print('show_all_hints')
    for each_grids in range(len(all_list_sep)):
        print('grid number:',each_grids+1)
        hits_number_for_print = 1
        for item in all_list_sep[each_grids]:
            print('hints number:',hits_number_for_print)
            hits_number_for_print += 1
            print(f'Put {item[0]} in location {item[1],item[2]}')

'''                    
def show_all_hints():

    for each_grids in range(len(all_list_sep)):
        file_name = f"Solution in text_{each_grids+1}.txt"  
        with open(file_name, 'w') as file:
                 file.write(f'grid number: {each_grids+1}\n')
                 hits_number_for_print = 1
                 for item in all_list_sep[each_grids]:
                     file.write(f'hints number: {hits_number_for_print}\n')
                     hits_number_for_print += 1
                     file.write(f'Put {item[0]} in location {item[1],item[2]}\n')


     
        
        
        
        
        
        
        
        
        
        
    
    
   