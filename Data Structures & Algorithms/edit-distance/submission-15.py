class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = list(range(n + 1))
        for i in range(1, m + 1):
            prev = dp[0] # i - 1/j - 1
            dp[0] = i
            for j in range(1, n + 1):
                temp = dp[j] # i - 1/j
                dp[j] = prev
                if word1[i - 1] != word2[j - 1]:
                   dp[j] = 1 + min(dp[j - 1], dp[j], temp)
                prev = temp # i - 1/j - 1 for next
        return dp[-1]