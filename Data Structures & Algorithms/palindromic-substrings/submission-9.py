class Solution:
    def countSubstrings(self, s: str) -> int:
        # s[l] == s[r] and inside = True
        # Edge Case: len <= 2 inside no need
        # Cond: every substring counts even if they read same substring 
        
        n = res = len(s) # count all char as + 1
        dp = [[False] * n for _ in range(n)]

        for r in range(1, n):
            for l in range(r - 1, -1, -1): # we grow outward, preventing counting single chars
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    res += 1
        return res