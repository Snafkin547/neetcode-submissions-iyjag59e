class TrieNode:
    def __init__(self, isword = False):
        self.children = {}
        self.isWord = isword

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def buildTrie(s):
            root = TrieNode()
            for c in reversed(s):
                curr = TrieNode(True)
                for k, v in root.children.items():
                    curr.children[k] = v
                root.children[c] = curr
            return root
        
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        root1 = buildTrie(text1)
        root2 = buildTrie(text2)
        res = 0
        q = deque()
        for k in root1.children.keys():
            if k in root2.children:
                q.append((root1.children[k], root2.children[k]))

        # Iterate for a smaller string
        curr = 1
        while q:
            for _ in range(len(q)):
                r1, r2 = q.popleft()
                for k in r1.children.keys():
                    if k in r2.children:
                        q.append((r1.children[k], r2.children[k]))
            res = max(res, curr)
            curr += 1
        return res

