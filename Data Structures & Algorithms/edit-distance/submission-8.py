class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # Cost of making non string
        dp = list(range(n + 1))
        
        for i in range(1, m + 1):
            next_dp = [0] * (n + 1)
            next_dp[0] = i
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    next_dp[j] = dp[j - 1]
                else:
                    next_dp[j] = 1 + min(dp[j - 1], next_dp[j - 1], dp[j])
            dp = next_dp
        return dp[-1]
