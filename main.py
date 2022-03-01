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

#this is taking a turn from player    
def player_turn():
    number_from_player = int(input("Current player, enter a number from one to nine: "))
    number_from_player = number_from_player - 1
    if board[number_from_player] == '-':
        board[number_from_player] = currentplayer
        board_game()
    else:
        print("That position was already taken")
        board_game()


#flips players from X to O
def flipplayer():
    global currentplayer
    #if player is O change to X
    if currentplayer == 'O':
        currentplayer = 'X'
    #if player is X change to O
    elif currentplayer == 'X':
        currentplayer = 'O'
    return


#if there are no mpre dashes then the games was a tie
def checks_if_tie():
    global winner
    global gameisgoingon
    if '-' not in board:
        gameisgoingon = False
        winner = None
        print("Tie")

# checks if a player won
def horizontally():
    global winner
    global gameisgoingon
    if board[0]== board[1]== board[2] and board[1] != '-':
        
    elif board[3]== board[4]== board[5] and board [2] != '-':
        winner = board[4]
        gameisgoingon = False
    elif board[6]== board[7]== board[8] and board[7] != '-':
        winner = board[7]
        gameisgoingon = False
    horizontally()

#checks for winner vertically
def check_vewrtically():
    global winner
    if board[0] == board[3] == board[6]:
        winner = board[0]
        return True



# use function to display board, add 'l' as border
def board_game():
    print(board[0] + ' l ' + board[1] + ' l ' + board[2])
    print(board[3] + ' l ' + board[4] + ' l ' + board[5])
    print(board[6] + ' l ' + board[7] + ' l ' + board[8])


#the main game
def playgame():
    while gameisgoingon: 
        player_turn()
        horizontally()
        flipplayer()
        checks_if_tie()  
playgame()




   






