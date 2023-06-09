#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 10:09:30 2023

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

def solve_sudoku(grid, possibilities):
    
    #set global value
    global width_empty_grid
    global Length_empty_grid
    global range_sudoku 
    
    #backtrack
    def backtrack(row, column):
        if row == range_sudoku:
            return grid

        next_row = row if column < range_sudoku-1 else row + 1
        next_column = (column + 1) % range_sudoku

        if grid[row][column] != 0:
            return backtrack(next_row, next_column)

        for value in possibilities[row][column]:
            if valid(row, column, value):
                grid[row][column] = value
                result = backtrack(next_row, next_column)
                if result is not None:
                    return result
                grid[row][column] = 0

        return None
    
    #test valid
    def valid(row, column, value):
        
        #set global value
        global width_empty_grid
        global Length_empty_grid
        global range_sudoku 
        
        for number_ in range(range_sudoku):
            if grid[row][number_] == value or grid[number_][column] == value:
                return False
        square_row = (row // width_empty_grid) * width_empty_grid
        square_column = (column // Length_empty_grid) * Length_empty_grid
        for row_ in range(square_row, square_row + width_empty_grid):
            for columm_ in range(square_column, square_column + Length_empty_grid):
                if grid[row_][columm_] == value:
                    return False
        return True

    return backtrack(0, 0)

def using_Wavefront(width_empty_grid_,Length_empty_grid_,grid_need_to_slove):
    
    #set global value
    global width_empty_grid
    global Length_empty_grid
    global range_sudoku
    
    width_empty_grid = width_empty_grid_
    Length_empty_grid = Length_empty_grid_
    range_sudoku = width_empty_grid * Length_empty_grid
    
  
    possible_values_for_grid = create_possible_values_grid(grid_need_to_slove)
    
    solution = solve_sudoku(grid_need_to_slove, possible_values_for_grid)
    
    
    return solution

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
    print(grid_need_to_slove)
    
    #find possible value
    possible_values_for_grid = create_possible_values_grid(grid_need_to_slove)
    print("\nAll possible value")
    print(possible_values_for_grid)
    
    #find solution
    solution = solve_sudoku(grid_need_to_slove, possible_values_for_grid)
    
    #print solution
    print('\nsolution\n',solution)
    
if __name__ == "__main__":
    main1()
