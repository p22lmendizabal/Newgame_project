#author: LM (AMDG) 2/7/22
# Tic Tac Toe project
# We need to make a board to play on
# Need to make X's and O's as markers
# Figure out hpw to place them
    #If somebody got three in a row

    #design of board 
# use list to design board
from turtle import pos


board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
# use function to display board, add 'l' as border
def board_game():
    print(board[0] + ' l ' + board[1] + ' l ' + board[2])
    print(board[3] + ' l ' + board[4] + ' l ' + board[5])
    print(board[6] + ' l ' + board[7] + ' l ' + board[8])
def playing():
    yesorno = str(input("Do you wish to play? Enter YES if yes or NO if no: ")).upper()
    if yesorno == 'YES':
       board_game()
       def player_turn():
            player_one_position = int(input("Enter a number from one to nine: "))
            player_one_position = player_one_position - 1
            board[player_one_position] = 'X'
            board_game()
            player_turn()
    elif yesorno == 'NO':
        print("Have a nice day!")






    

playing()


