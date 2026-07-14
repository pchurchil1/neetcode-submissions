class Solution:
    # Have to complete 3 checks:
    # Check each row: Hash each row, make sure there are no duplicates: for row in board
    # Check each column: Hash each col, make sure there are no duplicates: for col in board
    # Check each 3x3 box: Hash each grid, make sure there are no duplicates: 
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # Key = (row/3, col/3)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows[row] or
                    board[row][col] in cols[col] or
                    board[row][col] in squares[(row//3, col//3)]):
                    return False
                else:
                    cols[col].add(board[row][col])
                    rows[row].add(board[row][col])
                    squares[(row//3, col//3)].add(board[row][col])
        return True

