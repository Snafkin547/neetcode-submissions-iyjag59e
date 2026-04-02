class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Measure a longest subsequence and find a diff
        m, n = len(word1), len(word2)
        dp = [[-1] * n for _ in range(m)]

        def LIS(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i

            if dp[i][j] != -1:
                return dp[i][j]
            
            if word1[i] == word2[j]:
                dp[i][j] = LIS(i + 1, j + 1)
            else:
                dp[i][j] = 1 + min(LIS(i + 1, j + 1), LIS(i + 1, j), LIS(i, j + 1))
            return dp[i][j]
            
        return LIS(0, 0)