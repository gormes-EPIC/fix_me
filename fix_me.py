# Checks if a player wins the game and returns the winner
def is_winner(game):

    for i in range(3):
        # Check rows
        if (game[i][0] == game[i][1] == game[i][2] and game[i][0] != 0):
            if game[i][0] == 1:
                return 1
            return 2
        # Check columns
        if (game[0][i] == game[1][i] == game[2][i] and game[0][i] != 0):
            if game[0][i] == 1:
                return 1
            return 2
        # check diagonals
    if (game[0][0] == game[1][1] == game[2][2] and game[0][0] != 0):
        if game[0][0] == 1:
            return 1
        return 2
    if (game[0][2] == game[1][1] == game[2][0] and game[2][0] != 0):
        if game[0][2] == 1:
            return 1
        return 2
        
    # If no one wins return 0
    return 0

# Prints the board
def board(game):
    print(" --- --- --- ")
    for i in range(3):
        print("| " + str(game[i][0]) + " | " + str(game[i][1]) + " | " + str(game[i][2]) + " |")
        print(" --- --- --- ")

# Prompts user to make a move
def take_move(game, player):

    #Ask a given player for input
    move = input("Player " + str(player) + ", input a move at x,y: ")
    x,z = move.split(",")
    x = int(x) - 1
    z = int(z) - 1

    # If the move is legal, take the move and return the board
    if game[x][z] == 0:
        game[x][z] = player
        return game
    else: 
        print("Try Again Player " + str(player))
        take_move(game, player)    

# Run a TIc Tac Toe game
def main():
    # Start with an empty game board and player 1
    game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

    player = 1

    # Until someone wins, take moves and 
    
    while True:
        game = take_move(game, player)
        board(game)
        print()
        win = is_winner(game)
        if win == 1 or win == 2:
            break
    print("Player " + str(win) + " wins!")


main()
