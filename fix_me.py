def is_winner(game):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] != 0 or \
           game[0][i] == game[1][i] == game[2][i] != 0:
            return game[i][0]
    if game[0][0] == game[1][1] == game[2][2] != 0 or \
       game[0][2] == game[1][1] == game[2][0] != 0:
        return game[1][1]
    return 0

def print_board(game):
    # Print the game board
    print(" --- --- --- ")
    for row in game:
        print("| " + " | ".join(map(str, row)) + " |")
        print(" --- --- --- ")

def take_move(game, player):
    # Prompt user for a move
    while True:
        try:
            x, y = map(int, input(f"Player {player}, input a move at x,y (1-3): ").split(","))
            if 1 <= x <= 3 and 1 <= y <= 3 and game[x-1][y-1] == 0:
                game[x-1][y-1] = player
                break
            else:
                print("Invalid move.")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a comma.")

def main():
    # Initialize the game board
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    player = 1

    # Main game loop
    while True:
        print_board(game)
        take_move(game, player)
        winner = is_winner(game)
        if winner != 0:
            print_board(game)
            print(f"Player {winner} wins!")
            break
        player = 3 - player  # Switch player (1 -> 2, 2 -> 1)

if __name__ == "__main__":
    main()
