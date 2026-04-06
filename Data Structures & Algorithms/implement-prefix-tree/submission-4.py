class Node:
    def __init__(self, val = ""):
        self.val = val
        self.child = {} # char: Node
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        i = 0
        while i < len(word):
            if word[i] not in node.child:
                node.child[word[i]] = Node(word[i])
            node = node.child[word[i]]
            i += 1
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        i = 0
        while i < len(word) and word[i] in node.child:
            if i == len(word) - 1 and node.child[word[i]].isWord:
                return True
            node = node.child[word[i]]
            i += 1
        return False
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.child:
                return False
            node = node.child[char]
        return True
        
        