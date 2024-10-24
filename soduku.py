import math
grid = [[7,0,0,0,3,4,8,0,0],
        [8,0,4,6,0,0,0,0,0],
        [1,0,0,5,0,0,6,0,0],
        [0,4,0,7,0,9,0,3,0],
        [0,0,3,0,0,8,0,0,9],
        [0,0,0,0,7,0,3,2,0],
        [0,2,6,0,0,1,9,0,5],
        [0,0,7,9,2,0,0,0,4]]

size = len(grid)
print("grid size: ", size, " by ", size)
for row in range(size):
    print(grid[row])

area = int(math.sqrt(size))
print("area size: ", area, " by ", area)

# Display current grid
def display_grid():
    for i in range(size):
        print(grid[i])
    print()

# Check if number is in area
def check_area(num):
    section = 1
    section_contains_num = []

    for start_row in range(0, size, area):
        for start_col in range(0, size, area):
            end_row = start_row + area
            end_col = start_col + area
            contains_num = False

            for row in range(start_row, min(end_row, size)):
                for col in range(start_col, min(end_col, size)):
                    if grid[row][col] == num:
                        contains_num = True
            
            section_contains_num.append(contains_num)
            section += 1

    return section_contains_num

# Locate section a particular cell is in
def check_cell_area(i,j):
    section = 1
    for start_row in range(0, size, area):
        for start_col in range(0, size, area):
            end_row = start_row + area
            end_col = start_col + area
            
            if start_row <= i < end_row and start_col <= j < end_col:
                return section
            section += 1

#Check if a number is in a particular column
def check_col(num, col):
    for row in range(0, size):
        if(grid[row][col] == num):
           return True
    return False

#Check if a number is in a particular row
def check_row(num, row):
    for col in range(0, size):
        if(grid[row][col] == num):
           return True
    return False

#Check if a number can be placed in a cell
def check_cell(i,j):
    if(grid[i][j] == 0):
        for x in range(1,size+1):
            if is_valid(x, i, j):
                grid[i][j] = x
                print(f"Inserted {x} at position [{i}, {j}]")
                display_grid()
                return 

# Solves Soduku
def solve_soduku():
    solved = False
    while(solved == False):
        for i in range(size):
            for j in range(size):
             check_cell(i,j)
        solved = True
        for i in range(size):
            for j in range(size):
                if(grid[i][j]==0):
                    solved = False

#Checks if cell is valid 
def is_valid(num, i, j):
    if check_row(num, i):
        return False
    
    if check_col(num, j):
        return False

    section_index = check_cell_area(i, j) - 1
    if check_area(num)[section_index]:
        return False
    
    return True

#Start game and display final solution
def start_game():
    display_grid()
    solve_soduku()
    display_grid()         

start_game()






