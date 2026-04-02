class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m, n = len(word1), len(word2)
        dp = [0] * (n + 1)
        
        for j in range(n + 1):
            dp[j] = j  # Cost of inserting j characters to match word2 from empty word1

        for i in range(1, m + 1):
            temp = [0] * (n + 1)
            temp[0] = i # converting word1[:i] to empty string word2[:0]
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    temp[j] = dp[j - 1]
                else:
                    temp[j] = 1 + min(dp[j - 1], temp[j - 1], dp[j])
            dp = temp
        return dp[-1]