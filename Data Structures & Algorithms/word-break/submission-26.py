class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True
    
    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isEnd

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP bottom up/Trie
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        
        trie = Trie()
        t = 0
        for word in wordDict:
            trie.insert(word)
            t = max(t, len(word))
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i + 1, min(len(s), i + t) + 1):
                word = s[i: j]
                if trie.search(word):
                    dp[i] = dp[j]
                if dp[i]:
                    break
        return dp[0]