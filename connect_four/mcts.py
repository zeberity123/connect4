from connect_four import board, player, node
import sys, os
import random, math
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.wins = 0
        self.visits = 0

    def ucb1(self):
        if self.visits == 0:
            return float('inf')
        exploitation = self.wins / self.visits
        exploration = math.sqrt(math.log(self.parent.visits) / self.visits)
        return exploitation + exploration

class MCTS:
    def __init__(self, state):
        self.root = Node(state)

    def selection(self):
        node = self.root
        while node.children:
            node = max(node.children, key=lambda n: n.ucb1())
        return node

    def expansion(self, node):
        for move in node.state.get_legal_moves():
            next_state = node.state.apply_move(move)
            node.children.append(Node(next_state, node))

    def simulation(self, node):
        state = node.state
        while not state.is_game_over():
            move = random.choice(state.get_legal_moves())
            state = state.apply_move(move)
        return state.winner

    def backpropagation(self, node, outcome):
        while node:
            node.visits += 1
            if outcome == node.state.get_current_player():
                node.wins += 1
            node = node.parent

    def best_move(self):
        return max(self.root.children, key=lambda n: n.visits).state.last_move

    def run(self, simulations):
        for i in range(simulations):
            node = self.selection()
            if not node.state.is_game_over():
                if not node.children:
                    self.expansion(node)
                node = random.choice(node.children)
                outcome = self.simulation(node)
            else:
                outcome = node.state.winner
            self.backpropagation(node, outcome)