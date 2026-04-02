class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        w = set(wordDict)
        dp = {}
        
        def dfs(i):
            if i == n:
                return True

            if i in dp:
                return dp[i]
            
            dp[i] = False
            for k in range(i + 1, n + 1):
                if s[i:k] in w:
                    dp[i] |= dfs(k)
            return dp[i]
        return dfs(0)
