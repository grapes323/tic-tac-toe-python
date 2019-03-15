import random

#draw the game board 
def gameBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('___________')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('___________')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

#select who goes first, human or computer
#select random number 0 or 1, if 0 then computer goes first, else human goes first
def goesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'human'


#human selects the mark first, and the other mark will be the computer (X and O)
#create a list where the human mark is the first item, and computer second, upper case it.
#if not X or O then ask again
def humanMark():
    mark = ''
    while not (mark == 'X' or mark == 'O'):
        print('Will you be X or O?')
        mark = input().upper()

    if mark == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

#list out all possible combinations for a winner
def theWinner(board, mark):
    return (
        #horizontal top
        (board[1] == mark and board[2] == mark and board[3] == mark) or
        #horizontal middle
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        #horizontal bottom
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        #vertical left
        (board[1] == mark and board[3] == mark and board[5] == mark) or
        #vertical middle
        (board[2] == mark and board[4] == mark and board[6] == mark) or
        #vertical right
        (board[3] == mark and board[6] == mark and board[9] == mark) 
    )

