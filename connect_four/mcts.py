from connect_four import board, player, node
import sys, os
import random
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# class Mcts:
#     """Defines game tree for Connect 4
#     Contains fuctions for Monte-Carlo Tree Search.
#     """    
#     # def __init__(self, board, stone, loops, last_node=None):
#     #     """Inits by setting up the game tree.

#     #     Args:
#     #         board (Board): 2-dimensional array of board
#     #         stone (string): shape of marker 'O' or 'X' 
#     #         loops (int): number of iterations for the loops
#     #         last_node (Node, optional): last visited Node as selected. Defaults to None.
#     #     """        
#     #     print('inside function')
#     #     if last_node != None:
#     #         self.root = last_node
#     #     else:
#     #         self.root = node.Node(board.copy(), stone)
#     #     print('enter')
#     #     self.loops = loops
#     #     self.initial_board = board
#     #     self.stone = stone
#     #     print('random')

def random_move(input_board):
    game_board = board.Board()
    game_board.board = input_board
    free_columns = game_board.get_free_columns()
    if len(free_columns) == 0:
        return -1
    random_choice = random.choice(free_columns)
    return random_choice

def better_move(input_board):

    def winning_moves(temp_board, columns, stone):
        win_moves = []
        game_board = board.Board()
        game_board.board = temp_board

        for col in columns:
            row = game_board.get_free_row_index(col)
            game_board.add_stone(row, col, stone)
            if game_board.check_status(stone) == True:
                win_moves.append(col)
            game_board.add_stone(row, col, '_')

        return win_moves

    game_board = board.Board()
    game_board.board = input_board

    free_columns = game_board.get_free_columns()
    if len(free_columns) == 0:
        return -1

    win_moves = winning_moves(game_board.board, free_columns, 'X')
    lose_moves = winning_moves(game_board.board, free_columns, 'O')

    if len(win_moves) > 0:
        move = win_moves[0]
    elif len(lose_moves) > 0:
        move = lose_moves[0]
    else:
        move = random.choice(free_columns)

    return move