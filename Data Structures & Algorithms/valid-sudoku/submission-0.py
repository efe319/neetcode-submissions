class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = collections.defaultdict(set)
        row = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for n in range(9):
            for a in range(9):
                if board[n][a] == ".":
                    continue 
                if (board[n][a] in row[n] or board[n][a] in col[a] or board[n][a] in square[n // 3, a // 3]):
                    return False 
                row[n].add(board[n][a])
                col[a].add(board[n][a])
                square[n // 3, a // 3].add(board[n][a])
        return True