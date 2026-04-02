class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0
        for size in range(n):
            for i in range(n - size):
                dp[i][i + size] = (s[i] == s[i + size] and 
                    (
                        size < 2 or dp[i + 1][i + size - 1]
                    )
                )
                if dp[i][i + size]:
                    res += 1
        return res
