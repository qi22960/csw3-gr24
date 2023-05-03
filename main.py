#!/usr/bin/env python3
import time
import copy
import matplotlib.pyplot as plt
from Function_1_2_3 import show_hints
from Function_1_2_3 import read_file
from Function_1_2_3 import safe_file
from Function_1_2_3 import store_all_hints
from Function_1_2_3 import print_all_hints

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
    '''
	Solve function for Sudoku coursework.
	Comment out one of the lines below to either use the random or recursive solver
	'''

    # return random_solve(grid, n_rows, n_cols)
    return recursive_solve(grid, n_rows, n_cols)


def solve_time_average(grid, n_rows, n_cols):
    """
    This function measure time it takes for a grid to be solved for 10 times and calculate the average time
	args: grid
	return: average time in second
    """
    solve_times = []
    for a in range(5):
        start_time = time.time()
        solve(grid, n_rows, n_cols)
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


def variable_name(grid):
    """
    This function return the grid's name rather the grid
    args: grid
    return: grid name
    """
    for name, value in globals().items():
        if id(value) == id(grid):
            return name


def hints(hint_number):
    """
    This function return a selected number of hints to help solve the grids
    args: hint's number
    return: hints
    """
    show_hints(all_hints, hint_number)
    return 0


def main():
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
        safe_file("%d" % (i + 1), solution)  # task 2
        all_hints.append(['+++++++'])
        print('----------------')
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
    bar_width = 1
    # Plotting bars for each grid size. Time in y-axis and number of empty cells in x-axis
    ax.bar([h - bar_width / 3 for h in grid_2_2_empty], grid_2_2_time, width=bar_width, label="Grids (2x2)")
    ax.bar([h - bar_width / 3 for h in grid_2_3_empty], grid_2_3_time, width=bar_width, label="Grids (2x3)")
    ax.bar([h - bar_width / 3 for h in grid_3_3_empty], grid_3_3_time, width=bar_width, label="Grids (3x3)")
    # Title of the bar chart
    plt.title("Solve time vs Number of empty cells of all grids")
    # Axis labels and legend
    ax.set_xlabel('Number of empty cells')
    ax.set_ylabel('Solving time (second)')
    ax.legend()
    plt.show()
    plt.clf()

    # Bar chart of 2x2 grids
    plt.bar(grid_2_2_empty, grid_2_2_time, color=['blue'], width=0.5)
    plt.xlabel("Number of Empty cells")
    plt.ylabel("Solve time (s)")
    plt.title("2x2 Solve time vs Number of empty cells")
    plt.show()
    plt.clf()

    # Bar chart of 2x3 grids
    plt.bar(grid_2_3_empty, grid_2_3_time, color=['orange'], width=0.5)
    plt.xlabel("Number of Empty cells")
    plt.ylabel("Solve time (s)")
    plt.title("2x3 Solve time vs Number of empty cells")
    plt.show()
    plt.clf()

    # Bar chart of 3x3 grids
    plt.bar(grid_3_3_empty, grid_3_3_time, color=['green'], width=0.5)
    plt.xlabel("Number of Empty cells")
    plt.ylabel("Solve time (s)")
    plt.title("3x3 Solve time vs Number of empty cells")
    plt.show()

    # using flags:
    user_typing = 0
    while user_typing != 'quit':
        
        user_typing =input("\nYou can use flags  \nusing 'All hints' to show all hints, \nusing 'hints(number)' to show hints of the amount you need and the original grid with hints. Example: type 'hints(3)' to show 3 hints. \nusing 'plot' to show the solving time, \nusing 'store solution' to store the solution in text seperately,\nor type 'quit' to end\n-")
        #decide flag 'hints(number)' been used
        #take the number from input
        try:
            
            number_for_hints = int(user_typing.split("(")[1].split(")")[0])
            print(number_for_hints)
            hints(number_for_hints) 
            print("\nNumbers of hints has been show")
            
        except:
        #decide flag 'All hints' or 'plot' been used
            if user_typing == 'All hints':
                
                hints(0)  # task 3
                print_all_hints() # as files #task 1
                
            elif user_typing == 'plot':
                
                #show the graph 
                plot(grid_2_2_empty,grid_2_2_time,grid_2_3_empty,grid_2_3_time,grid_3_3_empty,grid_3_3_time)
                print("\nGraphs have been print")
                
            elif user_typing == 'store solution':
                
                hints(0)
                store_all_hints()
                print("\nThe text of hints has been store")
                
            elif user_typing == 'quit':
                
                print("\nend")
                
            else:
                print("\nInput error, please try again")


if __name__ == "__main__":
    main()
