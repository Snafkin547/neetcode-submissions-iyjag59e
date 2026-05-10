class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        curr = [["."] * n for _ in range(n)]
        col, posD, negD = set(), set(), set()
        
        def bt(r):
            # Base Case
            if r == n:
                res.append(["".join(r) for r in curr])
                return
            for c in range(n):
                if c in col or r + c in posD or r - c in negD:
                    continue
                col.add(c)
                posD.add(r + c)
                negD.add(r - c)
                curr[r][c] = "Q"
                bt(r + 1)
                col.remove(c)
                posD.remove(r + c)
                negD.remove(r - c)
                curr[r][c] = "."
        bt(0)
        return res