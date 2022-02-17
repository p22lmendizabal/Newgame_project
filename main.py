#author: LM (AMDG) 2/17/22
#Tic tac toe project 
# We need to make a board to play on
# Need to make X's and O's as markers
# Figure out hpw to place them
    #If somebody got three in a row

    #design of board 
# use list to design board

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
#there is no winner but it will be updated later
winner = None
currentplayer = 'O'
gameisgoingon = True
# use function to display board, add 'l' as border
def board_game():
    print(board[0] + ' l ' + board[1] + ' l ' + board[2])
    print(board[3] + ' l ' + board[4] + ' l ' + board[5])
    print(board[6] + ' l ' + board[7] + ' l ' + board[8])
#the main game
def playgame():
    while gameisgoingon: 
        #this is taking a turn from player    
        def player_turn():
            currentplayer = int(input("Current player, enter a number from one to nine: "))
            currentplayer = currentplayer - 1
            if board[currentplayer] == '-':
                board[currentplayer] = currentplayer
                board_game()
            elif board[currentplayer] == 'X':
                print("That position was already taken")
                board_game()  
        player_turn()

        def flipplayer():
            if currentplayer == 'O':
                currentplayer == 'X'
            elif currentplayer == 'X':
                currentplayer == 'O'
                return
        flipplayer()
playgame()
#checks if a player won or if the game is a tie



   

   






