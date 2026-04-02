class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()

        for word in wordDict:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.isEnd = True
        
        memo = set()
        n = len(s)

        def dfs(idx):
            if idx == n:
                return True
            if idx in memo:
                return False
            
            curr = root
            for j in range(idx, n):
                c = s[j]
                if c not in curr.children:
                    break
                curr = curr.children[c]

                if curr.isEnd:
                    if dfs(j+1):
                        return True
                    
            memo.add(idx)                        
            return False
        return dfs(0)