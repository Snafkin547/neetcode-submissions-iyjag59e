class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, arr = [], []

        # Create a DP matrix
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for size in range(n):
            for l in range(n - size):
                dp[l][l + size] = (s[l] == s[l + size] and 
                    (
                        size < 2 or
                        dp[l + 1][l + size - 1]
                    )
                )
        def dfs(i):
            if i >= len(s):
                res.append(arr[:])
                return
            for j in range(i, len(s)):
                if dp[i][j]:
                    arr.append(s[i:j + 1])
                    dfs(j + 1)
                    arr.pop()
        dfs(0)
        return res
                
                