class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]
        
        for i1 in range(len(text1) - 1, -1, -1):
            for i2 in range(len(text2) - 1, -1, -1):
               if text1[i1] == text2[i2]:
                   memo[i1][i2] = 1 + memo[i1 + 1][i2 + 1]
               else:
                   memo[i1][i2] = max(memo[i1 + 1][i2], memo[i1][i2 + 1])
        return memo[0][0]