import random

# Function to generate a maze with random walls and open spaces
def generate_maze(rows, cols):
    return [[1 if random.random() < 0.25 else 0 for _ in range(cols)] for _ in range(rows)]

# Function to print the maze in a readable format
def print_maze(maze):
    for row in maze:
        print(" ".join(str(cell) for cell in row))
    print()

# Recursive function to find the exit in the maze
def find_exit(maze, x, y, rows, cols):
    # Base case: If we have reached the bottom-right corner, return True
    if x == rows - 1 and y == cols - 1:
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

# Main function to execute the maze creation and pathfinding
def solve_maze(rows, cols):
    maze = generate_maze(rows, cols)
    print("Generated Maze:")
    print_maze(maze)
    
    if find_exit(maze, 0, 0, rows, cols):
        print("Path to exit found:")
    else:
        print("No path to exit exists.")
    
    print_maze(maze)

# Input for number of rows and columns
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Solve the maze
solve_maze(rows, cols)
