from pprint import pprint
from copy import deepcopy

def read_maze():
  '''read maze from the maze.txt, and return an array of maze'''
  filename = open("maze.txt", "r")
  array = list()
  for line in filename.readlines():
    array.append(list(line.strip()))
  filename.close()
  return array


def find_start(maze):
  '''find the start location, and return a tuple of the row, column location to "s" '''
  rows = len(maze)
  columns = len(maze[0])
  for row in range(rows):
    for column in range(columns):
      if maze[row][column] == 's':
        return row, column


def display_maze(maze, location):
  '''print row from maze'''
  # make a copy, so it won't affect the outside maze array

  maze_copy = deepcopy(maze)
  player_character = 'X'

  # change the start location symbol s to ' ', as it only uses as a reference
  start_row, start_col = find_start(maze_copy)
  maze_copy[start_row][start_col] = ' '

  # change the player location, to the player character
  player_row, player_column = location
  maze_copy[player_row][player_column] = player_character

  # 'character in between'.join(array)
  for row in maze_copy:
    print(''.join(row))


def display_menu():
  print("1. Up\n2. Down\n3. Left\n4. Right\n")


maze = read_maze()
player_row, player_col = find_start(maze)
# pprint(read_maze())
print("-Maze Solver-")

while maze[player_row][player_col] != 'f':
  # display maze
  display_maze(maze, (player_row, player_col))
  # display menu
  display_menu()
  # take user input for the direction
  try:
    direction = int(input('Enter your choice: '))
  except:
    print("Invalid input.")
    continue
  test_row, test_col = player_row, player_col
  # 1. up -> row - 1
  if direction == 1:
    test_row = player_row - 1
  # 2. down -> row + 1
  elif direction == 2:
    test_row = player_row + 1
  # 3. left -> col - 1
  elif direction == 3:
    test_col = player_col - 1
  # 4. right -> col + 1
  else:
    test_col = player_col + 1
  
  if maze[test_row][test_col] == '*':
    # say no
    print("Wall! Please have another choice.")
  else:
    # replace player row col, by assigning, test row, col to them
    player_row = test_row
    player_col = test_col
print("Congratulations! You solve the maze.")