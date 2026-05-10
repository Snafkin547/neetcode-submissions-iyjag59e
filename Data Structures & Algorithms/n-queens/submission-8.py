class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        curr = [["."] * n for _ in range(n)]
        col, posD, negD = [0] * n, [0] * 2 * n, [0] * 2 * n
        
        def bt(r):
            # Base Case
            if r == n:
                res.append(["".join(r) for r in curr])
                return
            for c in range(n):
                # n - r + n, + n is to avoid out of index issue when c > r
                if col[c] or posD[r + c] or negD[r - c + n]:
                    continue
                col[c] = True
                posD[r + c] = True
                negD[r - c + n] = True
                curr[r][c] = "Q"
                bt(r + 1)
                col[c] = False
                posD[r + c] = False
                negD[r - c + n] = False
                curr[r][c] = "."
        bt(0)
        return res