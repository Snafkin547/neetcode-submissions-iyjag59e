class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP from bottom up
        
        dp = [False] * (1+ len(s))
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                n = len(w)
                if i + n <= len(s) and s[i: i + n] == w:
                    dp[i] = dp[i + n]
                if dp[i]: # If true, move to next index
                    break
        return dp[0]
