#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 12:00:30 2023

@author: czm
"""

import random
import copy
import time
import csv
import numpy as np
import copy
import matplotlib.pyplot as plt
from Function_1_2_3  import show_hints
from Function_1_2_3  import read_file
from Function_1_2_3 import safe_file
from Function_1_2_3 import show_all_hints


'''
#Grids 1-4 are 2x2
grid1 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 3, 4],
		[3, 4, 2, 1]]

grid2 = [
		[1, 3, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 0, 4],
		[3, 4, 2, 1]]

grid3 = [
		[1, 0, 4, 2],
		[4, 2, 1, 0],
		[2, 1, 0, 4],
		[0, 4, 2, 1]]

grid4 = [
		[1, 0, 4, 2],
		[0, 2, 1, 0],
		[2, 1, 0, 4],
		[0, 4, 2, 1]]

grid5 = [
		[1, 0, 0, 2],
		[0, 0, 1, 0],
		[0, 1, 0, 4],
		[0, 0, 0, 1]]

grid6 = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]



grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2)]
#grid7 = read_file('easy1.txt')
#grid7 = read_file('hard1')

grid7 = [
[0, 2, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 6, 0, 4, 0, 0, 0, 0],
[5, 8, 0, 0, 9, 0, 0, 0, 3],
[0, 0, 0, 0, 0, 3, 0, 0, 4],
[4, 1, 0, 0, 8, 0, 6, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 9, 5],
[2, 0, 0, 0, 1, 0, 0, 8, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 3, 1, 0, 0, 8, 0, 5, 7]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2), (grid6,2,3), (grid7,3,3)]
'''

'''
grid1 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 3, 4],
		[3, 4, 2, 1]]

grid2 = [
		[1, 3, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 0, 4],
		[3, 4, 2, 1]]

grid3 = [
		[1, 0, 4, 2],
		[4, 2, 1, 0],
		[2, 1, 0, 4],
		[0, 4, 2, 1]]

grid4 = [
		[1, 0, 4, 2],
		[0, 2, 1, 0],
		[2, 1, 0, 4],
		[0, 4, 2, 1]]

grid5 = [
		[1, 0, 0, 2],
		[0, 0, 1, 0],
		[0, 1, 0, 4],
		[0, 0, 0, 1]]

grid6 = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]


grid7 = [
[8, 0, 9, 0, 2, 0, 3, 0, 0],
[0, 3, 7, 0, 6, 0, 5, 0, 0],
[0, 0, 0, 4, 0, 9, 7, 0, 0],
[0, 0, 2, 9, 0, 1, 0, 6, 0],
[1, 0, 0, 3, 0, 6, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 3],
[7, 0, 0, 0, 0, 0, 0, 0, 8],
[5, 0, 0, 0, 0, 0, 0, 1, 4],
[0, 0, 0, 2, 8, 4, 6, 0, 5]]


grid8 = [
[0, 2, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 6, 0, 4, 0, 0, 0, 0],
[5, 8, 0, 0, 9, 0, 0, 0, 3],
[0, 0, 0, 0, 0, 3, 0, 0, 4],
[4, 1, 0, 0, 8, 0, 6, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 9, 5],
[2, 0, 0, 0, 1, 0, 0, 8, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 3, 1, 0, 0, 8, 0, 5, 7]]


grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2), (grid6,2,3), (grid7,3,3), (grid8, 3, 3)]
'''
#task 2
grid1 = read_file('easy1.txt') #grid easy1
grid2 = read_file('easy2.txt') #grid easy1
grid3 = read_file('easy3') #grid easy1
grid4 = read_file('med1') #grid easy1
grid5 = read_file('med2') #grid easy1
grid6 = read_file('hard1') #grid easy1


grids = [(grid1, 3, 3), (grid2, 3, 3), (grid3, 2, 3), (grid4, 3, 3), (grid5, 3, 3), (grid6, 3, 3)]




def check_section(section, n):
    if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n + 1)]):
        return True
    return False


def get_squares(grid, n_rows, n_cols):
    squares = []
    for i in range(n_cols):
        rows = (i * n_rows, (i + 1) * n_rows)
        for j in range(n_rows):
            cols = (j * n_cols, (j + 1) * n_cols)
            square = []
            for k in range(rows[0], rows[1]):
                line = grid[k][cols[0]:cols[1]]
                square += line
            squares.append(square)

    return (squares)


# To complete the first assignment, please write the code for the following function
def check_solution(grid, n_rows, n_cols):
    '''
	This function is used to check whether a sudoku board has been correctly solved
	args: grid - representation of a suduko board as a nested list.
	returns: True (correct solution) or False (incorrect solution)
	'''
    n = n_rows * n_cols

    for row in grid:
        if check_section(row, n) == False:
            return False

    for i in range(n_rows ** 2):
        column = []
        for row in grid:
            column.append(row[i])

        if check_section(column, n) == False:
            return False

    squares = get_squares(grid, n_rows, n_cols)
    for square in squares:
        if check_section(square, n) == False:
            return False

    return True


def find_empty(grid):
    '''
	This function returns the index (i, j) to the first zero element in a sudoku grid
	If no such element is found, it returns None
	args: grid
	return: A tuple (i,j) where i and j are both integers, or None
	'''

    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if grid[i][j] == 0:
                return (i, j)

    return None


def possible_values(grid, n_rows, n_cols, position):
    all_rows = []
    [all_rows.append(i) for i in grid]
    rowss = all_rows[position[0]]

    column = []
    for row in grid:
        column.append(row[position[1]])

    for i in range(n_cols):
        rows = [i * n_rows, (i + 1) * n_rows]
        for j in range(n_rows):
            cols = [j * n_cols, (j + 1) * n_cols]
            if rows[0] <= position[0] < rows[1] and cols[0] <= position[1] < cols[1]:
                square = []
                for k in range(rows[0], rows[1]):
                    line = grid[k][cols[0]:cols[1]]
                    square += line

    not_possible = column + rowss + square

    possible = []
    for i in range(n_cols * n_rows + 1):
        if i not in not_possible:
            possible.append(i)

    return possible

#################################################################################################	
all_hints = []
#################################################################################################

def recursive_solve(grid, n_rows, n_cols):
    '''
	This function uses recursion to exhaustively search all possible solutions to a grid
	until the solution is found
	args: grid, n_rows, n_cols
	return: A solved grid (as a nested list), or None
	'''

    # N is the maximum integer considered in this board
    n = n_rows * n_cols
    # Find an empty place in the grid
    empty = find_empty(grid)

    # If there's no empty places left, check if we've found a solution
    if not empty:
        # If the solution is correct, return it.
        if check_solution(grid, n_rows, n_cols):
            return grid
        else:
            # If the solution is incorrect, return None
            return None
    else:
        row, col = empty

    # Loop through possible values
    for i in possible_values(grid, n_rows, n_cols, empty):
        

        # Place the value into the grid
        grid[row][col] = i
        # Recursively solve the grid
        ans = recursive_solve(grid, n_rows, n_cols)
        # If we've found a solution, return it
        if ans:
            # Print the location of empty cell and what number to fill with
            #print(f'Put {i} in location {row + 1, col + 1}')
            
#########################################################################################################
            all_hints.append([i,row+1,col+1])
            #print(all_hints)
#########################################################################################################  
          
            return ans

        # If we couldn't find a solution, that must mean this value is incorrect.
        # Reset the grid for the next iteration of the loop
        grid[row][col] = 0

    # If we get here, we've tried all possible values. Return none to indicate the previous value is incorrect.
    return None


def solve(grid, n_rows, n_cols):
    '''
	Solve function for Sudoku coursework.
	Comment out one of the lines below to either use the random or recursive solver
	'''

    # return random_solve(grid, n_rows, n_cols)
    return recursive_solve(grid, n_rows, n_cols)


def solve_time_average(grid, n_rows, n_cols):
    '''
    This function measure time it takes for a grid to be solved for 10 times and calculate the average time
	args: grid
	return: average time in second
    '''
    solve_times = []
    for a in range(5):
        start_time = time.time()
        solve(grid, n_rows, n_cols)
        finish_time = time.time()
        solve_times.append(finish_time - start_time)
        average_time = sum(solve_times) / len(solve_times)
    return average_time


def count_empty(grid):
    '''
    This function return the number of zeros/empty cells in the grid
	args: grid
	return: a number of zeros within a grid
    '''
    count = 0
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if grid[i][j] == 0:
                count = count + 1
    return count


def variable_name(grid):
    '''
    This function return the grid's name rather the grid
    args: grid
    return: grid name
    '''
    for name, value in globals().items():
        if id(value) == id(grid):
            return name
        
#######################################################################################################
def hits(hint_number):

    show_hints(all_hints,hint_number)
	
    return 0
#########################################################################################################


def main():
    #grd_number_for_test = 0
    points = 0

    # List of grids detail for bar chart
    grid_2_2_names = []
    grid_2_2_size = []
    grid_2_2_empty = []
    grid_2_2_time = []

    grid_2_3_names = []
    grid_2_3_size = []
    grid_2_3_empty = []
    grid_2_3_time = []

    grid_3_3_names = []
    grid_3_3_size = []
    grid_3_3_empty = []
    grid_3_3_time = []

    print("Running test script for coursework 1")
    print("====================================")

    for (i, (grid, n_rows, n_cols)) in enumerate(grids):
        print("Solving grid: %d" % (i + 1))
        start_time = time.time()
        new_grid = copy.deepcopy(grid)
        solution = solve(new_grid, n_rows, n_cols)
        elapsed_time = time.time() - start_time
        print("Solved in: %f seconds" % elapsed_time)
        print(solution)
        
#########################################################################################################
        #grd_number_for_test += 1
        safe_file("%d" % (i+1),solution) #task 2
        all_hints.append(['+++++++'])
        print('----------------')
######################################################################################################### 
 
        if check_solution(solution, n_rows, n_cols):
            print("grid %d correct" % (i + 1))
            points = points + 10
        else:
            print("grid %d incorrect" % (i + 1))

        # Append the name, size, number of empty cells and solve time of grid to list of each grid sizes
        if n_rows == 2 and n_cols == 2:
            grid_2_2_names.append(variable_name(grid))
            grid_2_2_size.append((n_rows, n_cols))
            grid_2_2_empty.append(count_empty(grid))
            grid_2_2_time.append(solve_time_average(grid, n_rows, n_cols))
        elif n_rows == 2 and n_cols == 3:
            grid_2_3_names.append(variable_name(grid))
            grid_2_3_size.append((n_rows, n_cols))
            grid_2_3_empty.append(count_empty(grid))
            grid_2_3_time.append(solve_time_average(grid, n_rows, n_cols))
        elif n_rows == 3 and n_cols == 3:
            grid_3_3_names.append(variable_name(grid))
            grid_3_3_size.append((n_rows, n_cols))
            grid_3_3_empty.append(count_empty(grid))
            grid_3_3_time.append(solve_time_average(grid, n_rows, n_cols))

    print("====================================")
    print("Test script complete, Total points: %d" % points)

    # Creating figure and axis objects
    fig, ax = plt.subplots()
    # Setting the width of each bars
    bar_width = 2
    # Plotting bars for each grid size. Time in y-axis and number of empty cells in x-axis
    ax.bar([h - bar_width / 3 for h in grid_2_2_empty], grid_2_2_time, width=bar_width, label="Grids (2x2)")
    ax.bar([h - bar_width / 3 for h in grid_2_3_empty], grid_2_3_time, width=bar_width, label="Grids (2x3)")
    ax.bar([h - bar_width / 3 for h in grid_3_3_empty], grid_3_3_time, width=bar_width, label="Grids (3x3)")
    # Axis labels and legend
    ax.set_xlabel('Number of empty cells')
    ax.set_ylabel('Solving time (second)')
    ax.legend()
    plt.show()
    
#########################################################################################################   
       
    hits(4) #task 3
    #print('all_hints',all_hints)
    show_all_hints()  #as files #task 1
    
#########################################################################################################

if __name__ == "__main__":
    main()