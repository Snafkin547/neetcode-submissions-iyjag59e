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
        for char in word:
            if char not in node.child:
                node.child[char] = Node(char)
            node = node.child[char]
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.child:
                return False
            node = node.child[char]
        return node.isWord
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.child:
                return False
            node = node.child[char]
        return True
        
        