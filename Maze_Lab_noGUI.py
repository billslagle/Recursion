# describe what the function does: tries to find an open path to go from upper left to lower right
# input requirements (pre-conditions): a 2-D maze of 1's (walls) and 0's (open); (x,y) coordinates of starting position;
#                                      a list of the path coordinates so far (start with empty list)
# output changes (post-conditions)
def find_path(maze, x, y, path=[]):
    ''' Function Definition:
    The function find_path is defined with 4 parameters:
    maze: A 2D list representing the maze: 0 represents an open path, 1 represents a wall, 
          and 8 represents a visited cell.
    x, y: The current coordinates in the maze (row, column))
    path: A list that keeps track of the path taken so far. It defaults to an empty list.
    '''
    
    if not (0 <= x < len(maze) and 0 <= y < len(maze[0])) or maze[x][y] in [1, 8]:
        return False
    ''' Boundary and Block Check:
    This if condition checks two things:
    1) Boundary Condition: (0 <= x < len(maze) and 0 <= y < len(maze[0])) checks if the current position (x, y) 
       is within the boundaries of the maze. If x or y is out of bounds, the function returns False.
    2) Wall or Visited Check: maze[x][y] in [1, 8] checks if the current cell is a wall (1) or has already been 
    visited (8). If either condition is true, the function returns False, indicating this path is not viable.
    '''
    
    if (x, y) == (len(maze) - 1, len(maze[0]) - 1):
        path.append((x, y))
        maze[x][y] = 8
        return True
    ''' Goal Check:
    This if condition checks if the current position (x, y) is the bottom-right corner of the maze, which is the goal.
    If the goal is reached:
       Append to Path: The current position (x, y) is added to the path list.
       Mark as Visited: The current cell maze[x][y] is marked as visited by setting it to 8.
       Return True: The function returns True, indicating that the path to the goal has been found.
    '''
    
    maze[x][y] = 8
    path.append((x, y))
    ''' Mark as Visited:
    If the function reaches this point, it means the current cell (x, y) is a valid and unvisited cell.
    The cell is marked as visited by setting maze[x][y] = 8.
    The current position (x, y) is also added to the path list.
    '''
    
    if any(find_path(maze, x + dx, y + dy, path) for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]):
        return True
    '''Recursive Exploration:
    This line recursively tries to move in one of the 4 possible directions: down, right, up, or left, by 
    adding dx and dy to x and y, respectively.
    The any function checks if any of these recursive calls return True, meaning a path to the goal was found in 
    one of the directions.
    If a valid path is found in any direction, the function returns True.
    '''
    
    maze[x][y] = 0
    path.pop()
    return False
    '''Backtrack:
    If the recursive exploration does not find a valid path, the function backtracks:
    Unmark Cell: current cell (x, y) is unmarked as visited by setting it back to 0: this path was not successful.
    Remove from Path: current position (x, y) is removed from the path list since it does not lead to the goal.
    The function returns False, indicating that no valid path to the goal was found from this position.
    '''

maze = [
    [0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
start_x, start_y = 0, 0
path = []

if find_path(maze, start_x, start_y, path):
    print("Path found:", path)  #if find_path returns True
else:
    print("No path found.")   #if find_path returns False

# Output the maze with the path marked '8'
print()
for row in maze:
    print(row)

# Example 1: Simple solvable maze
maze1 = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]

# Example 2: No solution (blocked maze)
maze2 = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1]
]

# Example 3: Single path maze
maze3 = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 0, 1, 1],
    [1, 0, 0, 0]
]

# Example 4: 1x1 maze (trivial case)
maze4 = [[0]]

# Example 5: Fully open maze
maze5 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Example 6: Start or end blocked
maze6 = [
    [1, 0, 0],
    [1, 1, 0],
    [1, 0, 0]
]


def test_find_path():
    test_cases = [
        (maze1, True),  # Solvable maze
        (maze2, False), # Unsolvable maze
        (maze3, True),  # Solvable maze
        (maze4, True),  # Solvable maze
        (maze5, True),  # Solvable maze
        (maze6, False)  # Unsolvable maze
    ]

    for i, (maze, expected) in enumerate(test_cases):
        path = []
        result = find_path(maze, 0, 0, path)
        print(f"Test Case {i+1}: {'Passed' if result == expected else 'Failed'}")
        if result:
            print(f"Path found: {path}")
        else:
            print("No path found")

test_find_path()
