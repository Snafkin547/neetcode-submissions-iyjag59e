class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2)+1)
        prev = [0] * (len(text2)+1)
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[j] = prev[j + 1] + 1
                else:
                    dp[j] = max(dp[j+1], prev[j])
            prev, dp = dp, prev
        return prev[0]