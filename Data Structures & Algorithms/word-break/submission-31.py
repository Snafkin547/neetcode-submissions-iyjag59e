class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        dp = [-1] * n
        def dfs(start):
            if start >= n:
                return True
            if dp[start]!=-1:
                return dp[start]
            for i in range(start + 1, n + 1):
                if s[start:i] in words and dfs(i):
                    dp[start] = True
                    return True
            dp[start] = False
            return False
        return dfs(0)
