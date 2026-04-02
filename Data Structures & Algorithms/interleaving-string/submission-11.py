class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l, m, n = len(s1), len(s2), len(s3)
        if l + m != n:
            return False
        dp = [[False] * (m + 1) for _ in range(l + 1)]

        for i in range(l + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1][-1]


