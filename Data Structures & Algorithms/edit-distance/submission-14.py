class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = list(range(n + 1))
        for i in range(1, m + 1):
            temp = [0] * (n + 1)
            temp[0] = i
            for j in range(1, n + 1):
                temp[j] = dp[j - 1]
                if word1[i - 1] != word2[j - 1]:
                   temp[j] = 1 + min(temp[j], dp[j], temp[j - 1])
            dp = temp
        return dp[-1]