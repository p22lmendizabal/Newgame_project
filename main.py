#author: LM (AMDG) 2/7/22
# Tic Tac Toe project
# We need to make a board to play on
# Need to make X's and O's as markers
# Figure out hpw to place them
    #If somebody got three in a row

while True:
    try:

        yesorno = input("Do you wish to play? If yes enter YES. If no enter NO: ").capitalize
        if yesorno == 'YES':
            continue
        elif yesorno == 'NO':
            break


#design of board 
# use list to design
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
# use function to display board, add 'l' as border
def board_game():
    print(board[0] + 'l' + board[1] + 'l' + board[2])
    print(board[3] + 'l' + board[4] + 'l' + board[5])
    print(board[6] + 'l' + board[7] + 'l' + board[8])

