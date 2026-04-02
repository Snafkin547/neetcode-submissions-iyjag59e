class TrieNode:
    def __init__(self, val, next= None):
        self.val = val
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root= TrieNode('-')
    
    def add(self, s):
        if not s:
            return

        curr = self.root
        
        
        for c in s:
            if c not in curr.children:
               curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        curr.is_word = True

    def find(self, s, i, j):
        curr = self.root
        for t in range(i, j):
            if s[t] in curr.children:
               curr = curr.children[s[t]]
            else:
                return False
        return curr.is_word

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        lgt = 0
        for w in wordDict:
            trie.add(w)
            lgt = max(lgt, len(w))
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for l in range(n):
            if not dp[l]:
                continue
            curr = trie.root
            for r in range(l + 1, min(l + 1 + lgt, n + 1)):
                if s[r - 1] in curr.children:
                    curr = curr.children[s[r-1]]
                else:
                    break
                if curr.is_word:
                   dp[r] = True
                   if r == n :
                      return True
        return dp[-1]
            