import math

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class Node:
    """Describes nodes for the game tree in MCTS.
    """    
    def __init__(self, board, stone, col=None, parent=None):
        """Inits by setting the attributes for selected node.

        Args:
            board (Board): 2-dimensional array of board
            stone (string): shape of marker 'O' or 'X' 
            col (int, optional): positional column index of the node. Defaults to None.
            parent (Node, optional): parent node of the current node. Defaults to None.
        """        
        self.col = col
        self.parentNode = parent
        self.stone = stone
        self.unused = board.get_free_columns()
        self.children = []
        self.wins = 0
        self.visits = 0

    def calc_ucb(self):
        """Calculates UCB value for the node.
        Uses UCB1 formula to calculate the values.

        Returns:
            Node: a child node that has the largest score UCB value.
        """        
        max_score, max_child = 0
        for child in self.children:
            score = child.wins / child.visits + math.sqrt(2*math.log(self.visits) / child.visits)
            if score > max_score:
                max_child = child
                max_score = score
        return max_child

    def add_child(self, col, board):
        node = Node(board.make_copy(), self.get_dif_stone(self.stone), col=col, parent=self)
        self.unused.remove(col)
        self.children.append(node)
        return node

        
    def get_dif_stone(self, stone):
        if stone == 'O':
            return 'X'
        else:
            return 'O'