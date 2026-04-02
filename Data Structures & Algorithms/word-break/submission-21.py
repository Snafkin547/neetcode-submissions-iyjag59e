class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP HashSet
        memo = set()

        def dfs(idx):
            if idx in memo:
                return False
            if idx >= len(s):
                return True
            
            for w in wordDict:
                if idx + len(w) <= len(s) and s[idx: idx + len(w)] == w:
                    if dfs(idx + len(w)):
                        return True
            memo.add(idx)
            return False
        return dfs(0)