class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # for loop the entire board
        # start recursion and flip the char to "-"
        # check the bkhndary 
        
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, i):
            if not (0 <= r < ROWS and 0 <= c < COLS) or board[r][c] != word[i]:
                return False
            if i == len(word) - 1 and board[r][c] == word[-1]:
                return True
            temp = board[r][c]
            board[r][c] = "-"
            res = dfs(r + 1, c, i + 1)| dfs(r - 1, c, i + 1) | dfs(r, c + 1, i + 1) | dfs(r, c - 1, i + 1)
            board[r][c] = temp
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False