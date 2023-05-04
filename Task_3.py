#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 12:17:39 2023

@author: czm
"""


from Function_1_2_3  import read_file
width_empty_grid = 0
Length_empty_grid = 0
range_sudoku = 0


def create_possible_values_grid(grid):
   
    #set global value
    global width_empty_grid
    global Length_empty_grid
    global range_sudoku 
    
    possible_values_grid = [[None if cell != 0 else list(range(1, range_sudoku+1)) for cell in row] for row in grid]
    #print(possible_values_grid)
    for row_number in range(range_sudoku):
        
        for column_number in range(range_sudoku):
            
            if grid[row_number][column_number] != 0:
                
                value = grid[row_number][column_number]
                
                # remove the value from the possible values of cells in the same row, column, and square
                for index in get_related_indices(row_number, column_number):
                    
                    if isinstance(possible_values_grid[index[0]][index[1]], list) and value in possible_values_grid[index[0]][index[1]]:
                        
                        possible_values_grid[index[0]][index[1]].remove(value)
                        
    return possible_values_grid

def get_related_indices(r, c):
    
    #set global value
    global width_empty_grid
    global Length_empty_grid
    global range_sudoku 
    
    related_indices = []
    for number_ in range(range_sudoku):
        
        # manage cells in the same column
        if number_ != r:
            related_indices.append((number_, c))  
            
        # manage cells in the same row   
        if number_ != c:
            related_indices.append((r, number_))
            
    square_row = (r // width_empty_grid) * width_empty_grid
    square_column = (c // Length_empty_grid) * Length_empty_grid
    for number_ in range(square_row, square_row + width_empty_grid):
        
        for l in range(square_column, square_column + Length_empty_grid):
        
            # manage cells in the same square
            if number_ != r and l != c:
                
                related_indices.append((number_, l))  
                
    return related_indices


    
def solve_sudoku(grid, possibles):
    '''
    find the least number of possibles and solved the suduku start from it
    '''
    #set global value
    global width_empty_grid
    global Length_empty_grid
    global range_sudoku 
       
    # Find the first empty cell with the min possible values.
    min_possibles_values = float('inf')
    next_row, next_column = None, None
    for row in range(range_sudoku):
           
        for column in range(range_sudoku):
            
            if grid[row][column] == 0 and len(possibles[row][column]) < min_possibles_values:
                
                min_possibles_values = len(possibles[row][column])
                next_row, next_column = row, column

    # find whether grid have been sloved
    if next_row is None and next_column is None:
        return True

    # Fit each possible value for the current cell.
    for value in possibles[next_row][next_column]:
           
        # Check if the value is valid in the current cell.
        if valid(grid, next_row, next_column, value):
               
            # Make the tentative assignment and recurse.
            grid[next_row][next_column] = value
            if solve_sudoku(grid, possibles):
                   
                return True
               
            #Undo the assignment.
            grid[next_row][next_column] = 0

    #backtrack.
    return False
    
#test valid
def valid(grid, row, column, value):
    
    """
    check whether the value is valid (follow the sudoku rows)
    """
    
    #set global value
    global width_empty_grid
    global Length_empty_grid
    global range_sudoku 
    
    # Check row.
    if value in grid[row]:
        return False
    
    # Check column.
    if value in [grid[number_][column] for number_ in range(range_sudoku)]:
        return False
    
    # Check subgrid.
    subgrid_row = (row // width_empty_grid) * width_empty_grid
    subgrid_col = (column // Length_empty_grid) * Length_empty_grid
    for number_r in range(subgrid_row, subgrid_row + width_empty_grid):
        
        for number_c in range(subgrid_col, subgrid_col + width_empty_grid):
            
            if grid[number_r][number_c] == value:
                return False
    
    return True

def using_Wavefront(width_empty_grid_,Length_empty_grid_,grid_need_to_slove):
    
    #set global value
    global width_empty_grid
    global Length_empty_grid
    global range_sudoku
    
    width_empty_grid = width_empty_grid_
    Length_empty_grid = Length_empty_grid_
    range_sudoku = width_empty_grid * Length_empty_grid
    
    #print(width_empty_grid)
    #print(Length_empty_grid)
    #print(range_sudoku)
    print("grid_need_to_slove:")
    print(grid_need_to_slove)
    
    #find possible value
    possible_values_for_grid = create_possible_values_grid(grid_need_to_slove)
    print("\nAll possible value:")
    print(possible_values_for_grid)
    
    #find solution
    solution = solve_sudoku(grid_need_to_slove, possible_values_for_grid)
    
    #print solution
    print('\nsolution:\n',solution,'\n')

def main1():
    
    #set global value
    global width_empty_grid
    global Length_empty_grid
    global range_sudoku
    
    #let user input the details of sudoku
    print("For test grid1 :easy1 copy.txt")
    print("For test grid2 :2x3.txt")
    print("For test grid3 :2x2.txt")
    file_name = input('please type the file name of the sudoku you want to test\n')
    width_empty_grid,Length_empty_grid = input("\nplease in put the range of sudoku. \nExample:\ntype '33' for 3*3\ntype '23' for 2*3\ntype '22' for 2*2\n")
    width_empty_grid = int(width_empty_grid)
    Length_empty_grid = int(Length_empty_grid)
    range_sudoku = width_empty_grid * Length_empty_grid
    
    #get the sudoku
    grid_need_to_slove = read_file(file_name)
    #print('\nThe empty grid:\n',grid_need_to_slove)
    
    #find possible value
    possible_values_for_grid = create_possible_values_grid(grid_need_to_slove)
    print("\nAll possible value:\n",possible_values_for_grid)
    
    #find solution
    solve_sudoku(grid_need_to_slove, possible_values_for_grid)
    solution = grid_need_to_slove
    
    #print solution
    print('\nsolution:\n',solution)
    
if __name__ == "__main__":
    main1()