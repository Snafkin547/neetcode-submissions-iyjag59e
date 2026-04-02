class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        t = max(len(x) for x in wordDict)
        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        l = 0
        for l in range(n):
            for r in range(l + 1, min(l + t + 1, n + 1)):
                if s[l:r] in wordDict and dp[l]:
                   dp[r] = True
        return dp[-1]
            