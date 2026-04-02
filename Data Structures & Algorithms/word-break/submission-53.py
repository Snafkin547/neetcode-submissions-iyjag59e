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

        dp = [False] * (n + 1) # True False indicates whether or not previous word ended there
        dp[0] = True # Base case for none
        i = 1
        for i in range(1, n + 1):
            # If just after a previous end
            if dp[i - 1]:
                node = root
                for j in range(i, n + 1):
                    if s[j - 1] in node.children:
                        node = node.children[s[j - 1]]
                        dp[j] |= node.is_word
                    else:
                        break
        return dp[-1]