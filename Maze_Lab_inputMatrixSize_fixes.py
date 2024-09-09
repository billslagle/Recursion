'''
CIST 5B: Lab Weeek 2, Group 8 (Sept 9, 2024)
This maze game assumes that the entrance is in the upper left corner.
The exit (goal) is in the lower right corner.
The user determines the size of the maze.
Walls are randomly selected.
'''
import random

# generate_maze() creates a 2-D maze with random walls and open spaces
# inputs: number of rows and columns for the maze size
# returns: list of 1's and 0's for the maze elements
def generate_maze(rows, cols):
    # uses list comprehension to create row-by-row
    # probability of a wall is 0.20 (too many walls for good play if 0.50)
    return [[1 if random.random() < 0.20 else 0 for _ in range(cols)] for _ in range(rows)]

# print_maze() displays a 2D maze in where each row is displayed with the cell values separated by spaces.
# inputs: a maze in the form of a 2D list of 1's and 0's
# returns: list of 1's and 0's for the maze el
def print_maze(maze):
    for row in maze:
        # recasts each integer as a string; joins the whole row as a string of numbers separated by a space.
        print(" ".join(str(cell) for cell in row))
    print()

# RECURSIVE FUNCTION: find_exit finds the exit in the maze (lower right corner)
# inputs: a 2D maze, current position (x, y), number of rows & columns in the maze
# returns: True if base case is reached; otherwise continues to check for next open space
def find_exit(maze, x, y, rows, cols):
    # BASE CASE: If we have reached the bottom-right corner and it's not a wall, return True
    if x == rows - 1 and y == cols - 1 and maze[x][y] == 0:
        maze[x][y] = 8  # Mark the exit as part of the path
        return True
    
    # Check if the current position is valid (within bounds and an open space)
    if x < 0 or x >= rows or y < 0 or y >= cols or maze[x][y] != 0:
        return False

    # Mark the current position as part of the solution path
    maze[x][y] = 8

    # Explore all possible directions: down, right, up, left
    if (find_exit(maze, x + 1, y, rows, cols) or  # Down
        find_exit(maze, x, y + 1, rows, cols) or  # Right
        find_exit(maze, x - 1, y, rows, cols) or  # Up
        find_exit(maze, x, y - 1, rows, cols)):   # Left
        return True

    # If none of the directions work, backtrack (unmark the current position)
    maze[x][y] = 0
    return False

# solve_maze primary function to execute the maze creation and pathfinding
# inputs: number of rows and columns for the maze
# output: displays the original maze and the path (if there is one)
def solve_maze(rows, cols):
    maze = generate_maze(rows, cols)
    print("\nGenerated Maze:")
    print_maze(maze)
    if find_exit(maze, 0, 0, rows, cols):
        print("Path to exit found:")
        print_maze(maze)
    else:
        print("No path to exit exists.\n")

# get_vaid_input() checks for valid inputs from the user for size of maze
# inputs: prompt for user inpjt
# returns: valid number of rows or columns
def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        # Check if input is non-empty and contains only digits
        if user_input.isdigit():
            value = int(user_input)
            # Ensure value is within the valid range
            if 1 <= value <= 20:
                return value
            else:
                print("Please enter a number between 1 and 20.")
        else:
            print("Invalid input. Please enter a non-negative integer with no spaces.")

# PLAY A GAME (main execution):
print("\nYou enter the maze in the upper left corner. Find a path to exit the lower right corner.")
# Input for number of rows and columns
rows = get_valid_input("Enter the number of rows in the maze (1 to 20): ")
cols = get_valid_input("Enter the number of columns in the maze (1 to 20): ")

# Solve the maze
solve_maze(rows, cols)
