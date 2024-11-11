#  CSPP EXAM PROJECT.
# BINGO GAME.
import random
#FUNCTION 1
def generateBoard():
    l=random.sample(range(1,101),25)                # used to generate a list from a specified range of specified count.
    board=[l[5*x:5*x+5] for x in range(5)]
    return board


#FUNCTION 2     
# Used to display the game board.
def displayBoard(board):
    for i in board:
        for j in i:
            print(j,end=" ")
        print()
    return None



#FUNCTION 3
# Code to mark the board with a given number.
def markNumber(board,number):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==number:
                board[i][j]="X"
                 
    return None


#FUNCTION 4
def getUserNumber():
    while True:
        try:
            n=int(input("Enter the drawn number: "))
            if n<1 or n>100:
                print("Enter a valid number in the range of 1-100")
            else:
                return n

        except:
            print("Invalid Input! Please enter a NUMBER.")


#FUNCTION 5
def checkWin(board):
    # return True or False
    allLines= vertlines(board)+horizlines(board)+diaglines(board)
    # print(allLines)
    for line in allLines:
        if line == ["X","X","X","X","X"]:
            return True
    return False

def vertlines(board):
    lines=[]
    for col in range(5):
        lines.append([board[0][col],board[1][col],board[2][col],board[3][col],board[4][col]])
    
    return lines

def horizlines(board):
    lines=[]
    for row in range(5):
        lines.append([board[row][0],board[row][1],board[row][2],board[row][3],board[row][4]])
    return lines
        
def diaglines(board):
    leftdown=[board[0][0] ,board[1][1] , board[2][2] , board[3][3] , board[4][4] ]
    rightdown=[board[0][4] , board[1][3] , board[2][2] , board[3][1] , board[4][0] ]
    return [leftdown,rightdown]


#FUNCTION 6
def playBingoGame():
    print("Hello Mate! Welcome to Bingo!")
    print()
    board=generateBoard()
    displayBoard(board)

    count=0
    while not checkWin(board):
        count+=1
        a=getUserNumber()
        markNumber(board,a)
        displayBoard(board)
 
    print("Congratulations! You've won the Game.")
    print("You took",count,"number of rounds to finish the Game.")

    return 

playBingoGame()

