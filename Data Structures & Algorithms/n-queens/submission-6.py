class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        curr = [["."] * n for _ in range(n)]
        
        def bt(r):
            # Base Case
            if r == n:
                res.append(["".join(r) for r in curr])
                return
            for c in range(n):
                if isSafe(r, c):
                    curr[r][c] = "Q"
                    bt(r + 1)
                    curr[r][c] = "."
        
        def isSafe(r, c):
            
            # Vertical
            row = r - 1
            while row >= 0:
                if curr[row][c] == "Q":
                    return False
                row -= 1
            
            # Diagonal Left
            row, col = r - 1, c - 1
            while row >= 0 and col >= 0:
                if curr[row][col] == "Q":
                    return False
                row -= 1
                col -= 1
            
            # Diagonal Right
            row, col = r - 1, c + 1
            while row >= 0 and col < n:
                if curr[row][col] == "Q":
                    return False
                row -= 1
                col += 1
            return True
        
        bt(0)
        return res