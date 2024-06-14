import tkinter as tk
from tkinter import messagebox

def initialize_grid(n):
    return [[" " for _ in range(n)] for _ in range(n)]

def is_valid_move(row, col, grid):
    return 0 <= row < len(grid) and 0 <= col < len(grid) and grid[row][col] == " "

def place_mark(sym, row, col, grid):
    grid[row][col] = sym

def check_win(grid, sym):
    all_lines = vertical_check(grid) + horizontal_check(grid) + diagonal_check(grid)
    return [sym] * len(grid) in all_lines

def vertical_check(grid):
    return [[grid[row][i] for row in range(len(grid))] for i in range(len(grid))]

def horizontal_check(grid):
    return [row for row in grid]

def diagonal_check(grid):
    left_right_diag = [grid[i][i] for i in range(len(grid))]
    right_left_diag = [grid[i][len(grid) - i - 1] for i in range(len(grid))]
    return [left_right_diag, right_left_diag]

def check_draw(grid):
    return all(cell != " " for row in grid for cell in row)

def switch_player(player):
    return "O" if player == "X" else "X"

def initialize_gui_grid(root, size):
    buttons = []
    for i in range(size):
        row = []
        for j in range(size):
            button = tk.Button(root, text=" ", font=('Helvetica', 20), width=5, height=2, 
                               bg="white", command=lambda i=i, j=j: on_button_click(i, j))
            button.grid(row=i+2, column=j)  # Offset rows to make space for the title and status
            row.append(button)
        buttons.append(row)
    return buttons

def on_button_click(row, col):
    global player, grid, buttons
    if is_valid_move(row, col, grid):
        place_mark(player, row, col, grid)
        color = "blue" if player == "X" else "red"
        buttons[row][col].config(text=player, state=tk.DISABLED, bg=color, disabledforeground="white")
        if check_win(grid, player):
            messagebox.showinfo("Tic Tac Toe", f"Player {player} wins!")
            reset_game()
        elif check_draw(grid):
            messagebox.showinfo("Tic Tac Toe", "The game is a draw!")
            reset_game()
        else:
            player = switch_player(player)
            update_status()

def reset_game():
    global grid, buttons, player
    grid = initialize_grid(len(grid))
    for row in buttons:
        for button in row:
            button.config(text=" ", state=tk.NORMAL, bg="white", fg="black")
    player = "X"
    update_status()

def update_status():
    status_label.config(text=f"Player {player}'s turn", fg=("blue" if player == "X" else "red"))

def play_game():
    global root, grid, buttons, player, status_label
    root = tk.Tk()
    root.title("Tic Tac Toe")

    size = int(input("Enter the size of the Grid (e.g., 3, 4, 5): "))
    grid = initialize_grid(size)
    player = "X"

    title_label = tk.Label(root, text="Tic Tac Toe", font=('Helvetica', 24, 'bold'))
    title_label.grid(row=0, column=0, columnspan=size)

    status_label = tk.Label(root, text=f"Player {player}'s turn", font=('Helvetica', 16), fg="blue")
    status_label.grid(row=1, column=0, columnspan=size)

    buttons = initialize_gui_grid(root, size)

    root.mainloop()

play_game()
