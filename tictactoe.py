#initialize variables
player = 1 
win = 1
running = 0
game = running
mark = 'X'
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] 
tie = -1


#draw game board
def gameBoard():
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('___________')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('___________')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    
#check if position is empty or not    
def checkPosition(x):
    if(board[x] == ' '):
        return True
    else:
        return False

#who is the winner
def theWinner():
    global game
    #horizontal top
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        game = win
    #horizontal middle
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        game = win
    #horizontal bottom
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        game = win
    #vertical left
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        game = win
    #vertical middle
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        game = win
    #vertical right
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        game = win
    #diagonal
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        game = win
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        game = win
    #tie if all positions are filled
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        game = tie
    else:
        game = running


print("Player 1 is [X], Player 2 is [O]")
print()
print("Numbers for each position:")
print()
print(' 1 | 2 | 3')
print('___________')
print(' 4 | 5 | 6')
print('___________')
print(' 7 | 8 | 9')
print()
print("Now let's play!")
print()

while(game == running):
    gameBoard()
    if(player % 2 != 0):
        print("Player 1's turn")
        mark = 'X'
    else:
        print("Player 2's turn")
        mark = 'O'
    choice = int(input("Type the position of you want to mark "))
    if(checkPosition(choice)):
        board[choice] = mark
        player+=1
        theWinner()
    
gameBoard()
if(game==tie):
    print("It's a tie!")
elif(game==win):
    player-=1
    if(player%2!=0):
        print("The winner is Player 1!!")
    else:
        print("The winner is Player 2!! Congratulations")