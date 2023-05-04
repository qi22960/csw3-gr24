#!/usr/bin/env python3
import argparse
import time
import copy
import matplotlib.pyplot as plt
from itertools import cycle
from Function_1_2_3 import show_hints
from Function_1_2_3 import read_file
from Function_1_2_3 import safe_file
from Function_1_2_3 import store_all_hints
from Function_1_2_3 import print_all_hints
from Task_3 import using_Wavefront

# 2x2 grids
grid1 = read_file('2x2_2.txt')
grid2 = read_file('2x2_4.txt')
grid3 = read_file('2x2_6.txt')
grid4 = read_file('2x2_8.txt')
grid5 = read_file('2x2_10.txt')
# 2x3 grids
grid6 = read_file('2x3_15.txt')
grid7 = read_file('2x3_20.txt')
grid8 = read_file('2x3_25.txt')
grid9 = read_file('2x3_30.txt')
# 3x3 grids
grid10 = read_file('easy1.txt')
grid11 = read_file('easy2.txt')
grid12 = read_file('med2.txt')
grid13 = read_file('med3.txt')
grid14 = read_file('hard1.txt')
grid15 = read_file('med1.txt')

grids = [
    (grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2),
    (grid6, 2, 3), (grid7, 2, 3), (grid8, 2, 3), (grid9, 2, 3),
    (grid10, 3, 3), (grid11, 3, 3), (grid12, 3, 3), (grid13, 3, 3), (grid14, 3, 3), (grid15, 3, 3)
    ]

grids_for_Wavefront_slove = copy.deepcopy(grids)

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
    """
    This function returns the index (i, j) to the first zero element in a sudoku grid
    If no such element is found, it returns None
    args: grid
    return: A tuple (i,j) where i and j are both integers, or None
    """

    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if grid[i][j] == 0:
                return (i, j)

    return None


def possible_values(grid, n_rows, n_cols, position):
    '''
    This function finds the possible values that could fill a given empty position and returns these possible values.

    args:
    grid - nested list
    n_rows - int
    n_cols - int
    position - function (find_empty(grid))

    returns:
    possible - list

    '''
    all_rows = []
    [all_rows.append(i) for i in grid]
    rowss = all_rows[position[0]] # List of all values in row of empty position

    column = [] # List of all values in column of empty position
    for row in grid:
        column.append(row[position[1]])

    for i in range(n_cols):
        rows = [i * n_rows, (i + 1) * n_rows]
        for j in range(n_rows):
            cols = [j * n_cols, (j + 1) * n_cols]
            if rows[0] <= position[0] < rows[1] and cols[0] <= position[1] < cols[1]: # True when the empty position is in the square
                square = [] # list of values in square of empty position
                for k in range(rows[0], rows[1]):
                    line = grid[k][cols[0]:cols[1]]
                    square += line

    not_possible = column + rowss + square  # Creates a list of all values in the row, column and square.
    # These values cannot be the value of empty position

    possible = [] # List of possible values of the empty position

    for i in range(n_cols * n_rows + 1):
        if i not in not_possible: # Only adds values which are not in list 'not_possible' to the list 'possible'
            possible.append(i)

    return possible # Returns the list 'possible'


all_hints = []


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
            all_hints.append([i, row + 1, col + 1])
            return ans

        # If we couldn't find a solution, that must mean this value is incorrect.
        # Reset the grid for the next iteration of the loop
        grid[row][col] = 0

    # If we get here, we've tried all possible values. Return none to indicate the previous value is incorrect.
    return None


def solve(grid, n_rows, n_cols):
    """
    Solve function for Sudoku coursework.
    Comment out one of the lines below to either use the random or recursive solver
    """
    #return wavefront_solve(grid, n_rows, n_cols)
    return recursive_solve(grid, n_rows, n_cols)


def average_solve_time(grid, n_rows, n_cols, solver_function):
    """
    This function measure time it takes for a grid to be solved using recursive solver and calculate the average 10 tries
    args: grid
    return: average time in second
    """
    solve_times = []
    grid_copy = copy.deepcopy(grid)
    for a in range(10):
        start_time = time.time()
        solver_function(grid_copy, n_rows, n_cols)
        finish_time = time.time()
        solve_times.append(finish_time - start_time)
        average_time = sum(solve_times) / len(solve_times)
    return round(average_time, 10)


def count_empty(grid):
    """
    This function return the number of zeros/empty cells in the grid
    args: grid
    return: a number of zeros within a grid
    """
    count = 0
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if grid[i][j] == 0:
                count = count + 1
    return count


def hints(hint_number):
    """
    This function return a selected number of hints to help solve the grids
    args: hint's number
    return: hints
    """
    show_hints(all_hints, hint_number)
    return 0


def profile():
    """
    This function collect information about grids such as size, number of empty cells
    and solution time of both recursive and wavefront solver
    Then it saves them in lists
    Then plot them in bar charts
    """
    # details of 2x2 grids
    grid_2_2_size = []
    grid_2_2_empty = []
    recursive_grid_2_2_time = []
    wavefront_grid_2_2_time = []

    # details of 2x3 grids
    grid_2_3_size = []
    grid_2_3_empty = []
    recursive_grid_2_3_time = []
    wavefront_grid_2_3_time = []

    # details of 3x3 grids
    grid_3_3_size = []
    grid_3_3_empty = []
    recursive_grid_3_3_time = []
    wavefront_grid_3_3_time = []

    # Append the grid size, number of empty cells and solve times of grid to lists of each grid sizes
    for (i, (grid, n_rows, n_cols)) in enumerate(grids):
        if n_rows == 2 and n_cols == 2:
            grid_2_2_size.append((n_rows, n_cols))
            grid_2_2_empty.append(count_empty(grid))
            recursive_grid_2_2_time.append(average_solve_time(grid, n_rows, n_cols, recursive_solve))
            wavefront_grid_2_2_time.append(average_solve_time(n_rows, n_cols, grid,  using_Wavefront))
        elif n_rows == 2 and n_cols == 3:
            grid_2_3_size.append((n_rows, n_cols))
            grid_2_3_empty.append(count_empty(grid))
            recursive_grid_2_3_time.append(average_solve_time(grid, n_rows, n_cols, recursive_solve))
            wavefront_grid_2_3_time.append(average_solve_time(n_rows, n_cols, grid,  using_Wavefront))
        elif n_rows == 3 and n_cols == 3:
            grid_3_3_size.append((n_rows, n_cols))
            grid_3_3_empty.append(count_empty(grid))
            recursive_grid_3_3_time.append(average_solve_time(grid, n_rows, n_cols, recursive_solve))
            wavefront_grid_3_3_time.append(average_solve_time(n_rows, n_cols, grid,  using_Wavefront))

    patterns = cycle(['/', '\\', '-', '+', 'x', 'o', 'O', '.', '*'])
    # Graph of 2x2 solution time vs number of unfilled cells
    x = range(len(grid_2_2_empty))
    width = 0.2
    fig, ax = plt.subplots()
    data1 = ax.bar(x, recursive_grid_2_2_time, width, label='Recursive 2x2')
    data2 = ax.bar([i + width for i in x], wavefront_grid_2_2_time, width, label='Wavefront 2x2')

    # Add pattern for overlapping bars
    for a, b in zip(data1, data2):
        if a.get_height() == b.get_height():
            b.set_hatch(next(patterns))

    # Customize plot
    ax.set_xticks([i + width / 2 for i in x])
    ax.set_xticklabels(grid_2_2_empty)
    ax.set_ylabel('Solving time (second)')
    ax.set_xlabel('Number of empty cells')
    ax.set_title('Solution time of 2x2 grids')
    ax.legend()

    # Graph of 2x3 solution time vs number of unfilled cells
    x = range(len(grid_2_3_empty))
    width = 0.2
    fig, ax = plt.subplots()
    data1 = ax.bar(x, recursive_grid_2_3_time, width, label='Recursive 2x3')
    data2 = ax.bar([i + width for i in x], wavefront_grid_2_3_time, width, label='Wavefront 2x3')

    # Add pattern for overlapping bars
    for a, b in zip(data1, data2):
        if a.get_height() == b.get_height():
            b.set_hatch(next(patterns))

    # Customize plot
    ax.set_xticks([i + width / 2 for i in x])
    ax.set_xticklabels(grid_2_3_empty)
    ax.set_ylabel('Solving time (second)')
    ax.set_xlabel('Number of empty cells')
    ax.set_title('Solution time of 2x3 grids')
    ax.legend()

    # Graph of 2x2 solution time vs number of unfilled cells
    x = range(len(grid_3_3_empty))
    width = 0.2
    fig, ax = plt.subplots()
    data1 = ax.bar(x, recursive_grid_3_3_time, width, label='Recursive 3x3')
    data2 = ax.bar([i + width for i in x], wavefront_grid_3_3_time, width, label='Wavefront 3x3')

    # Add pattern for overlapping bars
    for a, b in zip(data1, data2):
        if a.get_height() == b.get_height():
            b.set_hatch(next(patterns))

    # Customize plot
    ax.set_xticks([i + width / 2 for i in x])
    ax.set_xticklabels(grid_3_3_empty)
    ax.set_ylabel('Solving time (second)')
    ax.set_xlabel('Number of empty cells')
    ax.set_title('Solution time of 3x3 grids')
    ax.legend()
    plt.show()


def Wavefront_slove(grids):
    '''
    This function is used to use wavefrount slover in Task 3 to sloved the grids
    '''
    #print(grids_for_Wavefront_slove)
    #print(len(grids_for_Wavefront_slove))
    for grid_number in range(len(grids_for_Wavefront_slove)):
        print('\n=======================================')
        print('Wavefront_slove solution for grid',grid_number+1,':\n')
	#set grids need to be sloved
        grid_need_to_slove = grids_for_Wavefront_slove[grid_number][0]
	#set details of grids
        range_sudoku_ = grids_for_Wavefront_slove[grid_number][1]
        Length_empty_grid_ = grids_for_Wavefront_slove[grid_number][2]
	#using wavefront to slove suduku
        grid_been_sloved = using_Wavefront(range_sudoku_,Length_empty_grid_,grid_need_to_slove)
        print(grid_been_sloved)


def main():
    points = 0
    print("Running test script for coursework 1")
    print("====================================")

    for (i, (grid, n_rows, n_cols)) in enumerate(grids):
        print("Solving grid: %d" % (i + 1))
        new_grid = copy.deepcopy(grid)   # Make a copy of grids and solve them
        solve_times = []
        # Calculate the average solve time of 10 tries
        for a in range(10):
            start_time = time.time()
            solution = solve(new_grid, n_rows, n_cols)
            finish_time = time.time()
            solve_times.append(finish_time - start_time)
            average_time = sum(solve_times) / len(solve_times)
        print("Solved in: %.15f seconds" % average_time)
        print(solution)
        all_hints.append(['+++++++'])
        print('----------------')
        if check_solution(solution, n_rows, n_cols):
            print("grid %d correct" % (i + 1))
            points = points + 10
        else:
            print("grid %d incorrect" % (i + 1))

    print("====================================")
    print("Test script complete, Total points: %d" % points)
    profile()

    #using Wavefront to slove all grids
    Wavefront_slove(grids_for_Wavefront_slove)
    # using flags
    parser = argparse.ArgumentParser(description="Solve Sudoku")
    parser.add_argument("-explain", action="store_true", help="Show all the steps of the solving process")
    parser.add_argument("-hint", nargs="?", const=True, type=int, help="Show some specific hints by number")
    parser.add_argument("-profile", action="store_true", help="Show the plot of time")
    parser.add_argument('-file', nargs=2, help='input and output file paths,Example if you want read hard1 and safe it in solution for hard1 ,please use --file hard1.txt solution_for_hard1.txt')

    args = parser.parse_args()


    if args.explain == True:
        print('Show all hints1')
        hints(0)  # task 3
        print_all_hints() # as files #task 1
    else:
        print('Dont Show all hints')

    if args.hint is not None:
        if args.hint is True:
            number = True
            print('Show all hints')
            hints(0)  # task 3
            print_all_hints() # as files #task 1
        else:
            number = args.hint
            hints(number)
            print(number)

    if args.profile == True:
        print('show graphs')
        profile()

    else:
        print('Dont show graphs')

    if args.file:
        input_file_name, output_file_name = args.file
        print("Input file nmae:", input_file_name)
        #get grid which need to be slove
        gride_to_slove_ = read_file(input_file_name)
        #ger detials of grid
        if len(gride_to_slove_) > 6:
            row = 3
            column = 3
        elif len(gride_to_slove_) == 6:
            row = 2
            column = 3
        else:
            row = 2
            column = 2
        #get sloved grid
        solved_grid = using_Wavefront(row,column,gride_to_slove_)


        print("Output file name:", output_file_name)

        #print(type(output_file_path))
        #safe sloved grad
        safe_file(output_file_name,solved_grid)

        if args.explain == True:
            hints(0)
            store_all_hints(output_file_name)


if __name__ == "__main__":
    main()
