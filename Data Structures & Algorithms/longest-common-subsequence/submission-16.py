class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        curr = [0] * (len(text2) + 1)
        
        for i1 in range(len(text1) - 1, -1, -1):
            prev = 0
            for i2 in range(len(text2) - 1, -1, -1):
                tmp = curr[i2]
                if text1[i1] == text2[i2]:
                   curr[i2] = 1 + prev
                else:
                   curr[i2]= max(curr[i2], curr[i2 + 1])
                prev = tmp
        return curr[0]