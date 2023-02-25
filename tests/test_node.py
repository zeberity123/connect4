from cgi import test
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from unittest import TestCase, main
from connect_four import board, player, node

game_board = board.Board()
game_player = player.Player()

class NodeTests(TestCase):

    def test0_board_row(self):
        print('\n')
        game_board = board.Board()
        game_player = player.Player()
        testNode = node.Node(game_board, game_player.stone)
        self.assertEqual(testNode.stone, 'O')
        self.assertIsNone(testNode.parentNode)
        self.assertIsNone(testNode.col)
        for i in range(6):
            game_board.board[i][3] = 'O'
        game_board.print_board()
        testNode = node.Node(game_board, game_player.stone)
        self.assertEqual(testNode.unused, [0,1,2,4,5,6])
        

if __name__ == '__main__':
    main()