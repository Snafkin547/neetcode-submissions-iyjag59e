class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = set()
        n = len(s)
        def dfs(idx):
            if idx in memo:
                return False
            if idx >= n:
                return True

            for word in wordDict:
                if idx + len(word) <= n and s[idx: idx + len(word)] == word:
                    if dfs(idx+ len(word)):
                        return True
            memo.add(idx)
            return False
        return dfs(0)