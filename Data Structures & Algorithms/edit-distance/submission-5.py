class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m, n = len(word1), len(word2)
        dp = [0] * (n + 1)
        
        for j in range(n + 1):
            dp[j] = j  # Cost of inserting j characters to match word2 from empty word1

        for i in range(1, m + 1):
            prev = dp[0] # converting word1[:i] to empty string word2[:0]
            dp[0] = i
            for j in range(1, n + 1):
                temp = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = 1 + min(dp[j - 1], prev, dp[j])
                prev = temp
        return dp[-1]