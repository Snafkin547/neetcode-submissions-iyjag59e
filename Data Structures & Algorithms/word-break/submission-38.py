class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[-1] = True
        for l in range(n - 1, -1, -1):
            for w in wordDict:
                if l + len(w) <= n and s[l:l + len(w)] == w:
                   dp[l] = dp[l + len(w)]
                
                if dp[l]:
                    break
        return dp[0]
            