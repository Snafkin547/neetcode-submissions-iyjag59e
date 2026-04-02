class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP HashSet
        memo = {}
        wordSet = set(wordDict)
        t = 0
        for w in wordDict:
            t = max(t, len(w))

        def dfs(idx):
            if idx in memo:
                return memo[idx]
            if idx == len(s):
                return True
            
            for j in range(idx, min(len(s), idx + t)):
                if s[idx : j + 1] in wordSet:
                    if dfs(j + 1):
                        memo[idx] = True
                        return True
            memo[idx] = False
            return False
        return dfs(0)