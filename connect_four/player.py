from player import Player

# Create two players, one using the MCTS algorithm and one using a simple heuristic
player1 = Player(color=1, depth=None, algorithm='MCTS')
player2 = Player(color=2, depth=3, algorithm='simple_heuristic')

# Play the game with the two players
board = [[0] * 7 for _ in range(6)]
current_player = player1
while True:
    print_board(board)
    if current_player is None:
        print("It's a draw!")
        break
    if current_player.color == 1:
        move = current_player.get_move(board)
        print(f"Player 1 chooses column {move}")
    else:
        move = int(input("Player 2 choose a column (0-6): "))
    if is_valid_move(board, move):
        drop_piece(board, move, current_player.color)
        if is_win(board, current_player.color):
            print_board(board)
            print(f"Player {current_player.color} wins!")
            break
        current_player = player2 if current_player == player1 else player1
    else:
        print("Invalid move. Please try again.")