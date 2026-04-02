class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        arr = [0] * 9
        rows = {i: arr.copy() for i in range(9)}
        cols = {i: arr.copy() for i in range(9)}
        grid = {(x, y): arr.copy() for x in range(3) for y in range(3)}
        for i in range(81):
            r = i//9
            c = i%9

            if board[r][c] == ".":
                continue

            val = int(board[r][c])
            if rows[r][val - 1] or cols[c][val - 1] or grid[(r//3, c//3)][val - 1]:
                return False
            rows[r][val - 1] = cols[c][val - 1] = grid[(r//3, c//3)][val - 1] = 1
        return True