class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [0] * len(text1)
        
        def dfs(i1, i2):
            if i1 == len(text1) or i2 == len(text2):
                return 0
            if memo[i1]:
                return memo[i1]
            res = 0
            for idx in range(i1, len(text1)):
                for idx2 in range(i2, len(text2)):
                    if text1[idx] == text2[idx2]:
                       res = max(res, 1 + dfs(idx + 1, idx2 + 1))
                       break
            memo[i1] = res
            return res
        return dfs(0, 0)
                    