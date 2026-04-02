class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # State i, j
        # Ops, move i or j
        l, m, n = len(s1), len(s2), len(s3)
        if l + m != n:
            return False
        dp = {}
        def helper(i, j):
            if i + j == n:
                return True
            if (i, j) in dp:
                return dp[(i, j)]

            dp[(i, j)] = False
            if i < l and s1[i] == s3[i + j]:
                dp[(i, j)] |= helper(i + 1, j)
            if j < m and s2[j] == s3[i + j]:
                dp[(i, j)] |= helper(i, j + 1)
            return dp[(i, j)]
        return helper(0, 0)