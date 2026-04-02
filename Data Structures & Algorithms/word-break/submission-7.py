class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = set()

        def dfs(idx):
            if idx >= len(s):
                return True
            if idx in memo:
                return False
                
            for word in wordDict:
                n = len(word)
                if idx + n <= len(s) and s[idx: idx + n] == word:
                    if dfs(idx + n):
                        return True
            memo.add(idx)                        
            return False
        return dfs(0)