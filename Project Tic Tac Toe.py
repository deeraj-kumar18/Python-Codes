def initialize_grid(n):
    grid=[]
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(" ")
        grid.append(row)
    
    return grid

def print_grid(grid):
    n=len(grid)
    for row in grid:
        print(" | ".join(row))
        print("-" * (n * 2 + (n)))

        
def get_user_input():
    while True:
        try:
            row,col=map(int,input("Enter the row and col number of the grid, where you want to mark it. ").split())
            return row-1,col-1   # for Zero indexing
        except ValueError:
            print("Invalid Input. Enter two numbers separated by Space.")

def is_valid_move(row,col,grid):
    n=len(grid)
    if 0<=row<=n and 0<=col<=n and grid[row][col] == " ":
        return True
    return False
          
def place_mark(sym,row,col,grid):
    grid[row][col]=sym
    
def check_win(grid,sym):
    all_lines=vertical_check(grid)+horizontal_check(grid)+diagonal_check(grid)
    if [sym]*len(grid) in all_lines:
        return True
    return False

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
    return all(cell != " " for row in grid for cell in row)

def switch_player(player):
    if player=="X":
        player="O"
    else:
        player="X"
    return player

def play_game():
    print("Welcome to Tic Tac Toe!")
    print("This is a 2 Player Game. \n Player 1 has the Symbol 'X' \n Player 2 has the Symbol 'O' ")
    size=int(input("Enter the size of the Grid(eg:3,4,5): "))
    grid=initialize_grid(size)
    player="X"
    while True:
        print_grid(grid)
        print(f"This is Player {player}'s turn")
        while True:
            row,col=get_user_input()
            if is_valid_move(row,col,grid):
                break
            else:
                print("Invalid Move. Try Again")
        
        place_mark(player,row,col,grid)

        if check_win(grid,player):
            print_grid(grid)
            print(f"Player {player} wins!.")
            break
        
        if check_draw(grid):
            print_grid(grid)
            print("The game is a draw!")
            break
        
        player = switch_player(player)



        


play_game()
