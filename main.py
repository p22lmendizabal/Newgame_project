#author: LM (AMDG) 2/7/22
# Tic Tac Toe project
# We need to make a board to play on
# Need to make X's and O's as markers
# Figure out hpw to place them
    #If somebody got three in a row

    #design of board 
# use list to design board

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
# use function to display board, add 'l' as border
def board_game():
    print(board[0] + ' l ' + board[1] + ' l ' + board[2])
    print(board[3] + ' l ' + board[4] + ' l ' + board[5])
    print(board[6] + ' l ' + board[7] + ' l ' + board[8])

#this is taking a turn from player    
def player_turn():
    while True:
        try:
            player_one_position = int(input("Player one, enter a number from one to nine: "))
            player_one_position = player_one_position - 1
            if board[player_one_position] == '-':
                board[player_one_position] = 'O'
            elif board[player_one_position] == 'X':
                print("That position was already taken")
                player_one_position
            board_game()
            player_two_position = int(input("Player two, enter a number from one to nine: "))
            player_two_position = player_two_position - 1
            if board[player_two_position] == '-':
                board[player_two_position] = 'X'
            elif board[player_two_position] == 'O':
            
        except:
            print("That spot is already taken")

        board_game()
player_turn()

#checks if a player won or if the game is a tie



   

   






