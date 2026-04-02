class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        root = TrieNode()
        t = 0
        for w in wordDict:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.is_word = True
            t = max(t, len(w))

        dp = {}
        
        def dfs(i):
            if i == n:
                return True

            if i in dp:
                return dp[i]
            
            dp[i] = False
            node = root
            
            for k in range(i, n):
                if s[k] in node.children:
                    node = node.children[s[k]]
                    if node.is_word:
                        dp[i] |= dfs(k + 1)
                else:
                    break
            return dp[i]
        return dfs(0)
