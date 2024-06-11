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
    print(row,col)

