class TreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not curr.children[i]:
                curr.children[i] = TreeNode()
            curr = curr.children[i]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
             i = ord(c) - ord('a')
             if not curr.children[i]:
                break
             curr = curr.children[i]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if not curr.children[i]:
                return False
            curr = curr.children[i]
        return True
        