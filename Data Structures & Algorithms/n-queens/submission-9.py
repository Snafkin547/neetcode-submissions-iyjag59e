class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        curr = [["."] * n for _ in range(n)]
        
        def bt(r, col, posD, negD):
            # Base Case
            if r == n:
                res.append(["".join(r) for r in curr])
                return
            for c in range(n):
                # n - r + n, + n is to avoid out of index issue when c > r
                if col & 1 << c or posD & 1 << (r + c) or negD & 1 << (r - c + n):
                    continue
                curr[r][c] = "Q"
                bt(r + 1, col | 1 << c, posD | 1 << (r + c), negD | 1 << (r - c + n))
                curr[r][c] = "."
        bt(0, 0, 0, 0)
        return res