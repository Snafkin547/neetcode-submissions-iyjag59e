class Node:
    def __init__(self):
        self.child = {}
        self.isWord = False

class WordDictionary:
    # If c == ".", need all children : when adding a child, also add the same node to dot
    # Keep prev/parent node, reference its dot node. This node has all children of the same layer, including child "."

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.child:
                node.child[c] = Node()
            node = node.child[c]
        node.isWord = True
    
    def search(self, word: str) -> bool:
        def dfs(idx, root):
            node = root
            for i in range(idx, len(word)):
                c = word[i]
                if c == ".":
                    for child in node.child.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in node.child:
                        return False
                    node = node.child[c]
            return node.isWord
        return dfs(0, self.root)
