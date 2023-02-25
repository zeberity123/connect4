class Board:
    """Describes the game board for connect 4.
    """    
    def __init__(self):
        """Creates a game board.
        The board will be size of 6 rows and 7 columns.
        Each blanks of the list will be filled by '_' initially. 
        """        
        self.row = 6
        self.col = 7
        self.board = [['_' for i in range(self.col)] for j in range(self.row)]
        self.count = 0
    
    def print_board(self):
        """Prints the game board on command line with column numbers.
        """        
        for i in self.board[::-1]:
            print(i)
        print('-----------------------------------')
        print("  0    1    2    3    4    5    6")

    def add_stone(self, row, column, stone):
        """Places a stone at the specific given position on the board.

        Args:
            row (int): row number from 0 to 5
            column (int): column number from 0 to 6
            stone (string): shape of marker 'O' or 'X'
        """        
        self.board[row][column] = stone
        self.count += 1

    def get_free_row_index(self, column_index):
        """Returns the position of empty row index in the column

        Args:
            column_index (int): column number from 0 to 6

        Returns:
            int: empty row index (from 0 to 5) or -1 if the column is full
        """        
        for row_index in range(self.row):
            if self.board[row_index][column_index] == '_':
                return row_index
        return -1
    
    def get_free_columns(self):
        """Returns list of columns which are not full

        Returns:
            list: list of column numbers from 0 to 6
        """        
        free_columns = []
        for column_index in range(self.col):
            if self.get_free_row_index(column_index) != -1:
                free_columns.append(column_index)
        return free_columns

    def put_stone(self, column_index, stone):
        """Places stone on the board at corresponding column's lowest empty row.

        Args:
            column_index (int): column number from 0 to 6
            stone (string): shape of marker 'O' or 'X'
        """        
        row_index = self.get_free_row_index(column_index)
        self.board[row_index][column_index] = stone
        self.count += 1
    
    def check_status(self, stone):
        """Checks whether there is any win state on the board.
        There are 4 types of winning states; Horizontal(-), Vertical (|), Diagonal(/) and another Diagonal(\).
        If the board has any types of winning state described above, returns True.

        Args:
            stone (string): shape of marker 'O' or 'X'

        Returns:
            boolean: True if there is a winning state, if not, False.
        """        
        # 1 Horizontal (-)
        for col in range(self.col - 3):
            for row in range(self.row):
                if self.board[row][col] == stone and self.board[row][col + 1] == stone and \
                    self.board[row][col + 2] == stone and self.board[row][col + 3] == stone:
                    return True

        # 2 Vertical (|)
        for col in range(self.col):
            for row in range(self.row - 3):
                if self.board[row][col] == stone and self.board[row + 1][col] == stone and \
                    self.board[row + 2][col] == stone and self.board[row + 3][col] == stone:
                    return True
        
        # 3 Diagonal (/)
        for col in range(self.col - 3):
            for row in range(self.row - 3):
                if self.board[row][col] == stone and self.board[row + 1][col + 1] == stone and \
                    self.board[row + 2][col + 2] == stone and self.board[row + 3][col + 3] == stone:
                    return True
        # 4 Diagonal (\)
        for col in range(self.col - 3):
            for row in range(3, self.row):
                if self.board[row][col] == stone and self.board[row - 1][col + 1] == stone and \
                    self.board[row - 2][col + 2] == stone and self.board[row - 3][col + 3] == stone:
                    return True

    def is_board_full(self):
        """Checks if the board is full or not

        Returns:
            Boolean: True if the board is full, if not, False.
        """        
        if self.count == 42:
            return True
        return  False