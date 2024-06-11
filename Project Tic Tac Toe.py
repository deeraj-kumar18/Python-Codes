def initialize_grid(n):
    grid=[]
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(" * ")
        grid.append(row)
    
    return grid

def print_grid(grid):
    for row in grid:
        for ele in row:
            print(ele,end=" ")
        print()

        
def get_user_input():
    row,col=map(int,input("Enter the row and col number of the grid, where you want to mark it. ").split())
    return row,col

def place_mark(sym,row,col,grid):
    grid[row][col]=sym
    
def check_win(grid):
    all_lines=vertical_check(grid)+horizontal_check(grid)+diagonal_check(grid)

    player_x = ["X"]*len(grid)
    player_o = ["O"]*len(grid)

    if player_x  in all_lines:
        return "Player X wins."
    elif player_o in all_lines:
        return "Player O wins."

def vertical_check(grid):
    cols=[]
    for i in range(len(grid)):
        col=[]
        for row in range(len(grid)):
            col.append(grid[row][i])
        cols.append(col)
    return cols

def horizontal_check(grid):
    rows=[]
    for row in grid:
        rows.append(list(row))
    return rows

def diagonal_check(grid):  
    diag=[]
    left_right_diag=[]
    for i in range(len(grid)):
        left_right_diag.append(grid[i][i])
    
    right_left_diag=[]
    for i in range(len(grid)):
            right_left_diag.append(grid[i][len(grid)-i-1])

    diag.append(left_right_diag)
    diag.append(right_left_diag)
    return diag

def check_draw(grid):
    return

def switch_player(player):
    if player=="p1":
        return "p2"
    else:
        return "p1"

def play_game():
    while True:
        
        grid=initialize_grid()
# b=[["X","e","X"],["W","W","z"],["O","O","O"]]
# a=check_win(b)
# print(a)
