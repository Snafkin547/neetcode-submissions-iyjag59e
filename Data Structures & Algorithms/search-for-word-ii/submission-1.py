class Trie:
    def __init__(self):
        self.root = TrieNode()

    def buildTree(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = word

    def startWith(self, c):
        return c in self.root.children
    
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None        
    
    def isChild(self, c):
        return c in self.children

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.buildTree(word)
        res = set()
        visiting = set()
        # Iterate with visiting grid
        ROWS, COLS = len(board), len(board[0])
        for row in range(ROWS):
            for col in range(COLS):        
                if trie.startWith(board[row][col]):
                    stack = [(row, col, trie.root.children[board[row][col]], False)]
                     
                    while stack:
                        r, c, node, isBT = stack.pop()
                        
                        # Coming back
                        if isBT:
                            visiting.remove((r, c))
                            continue
                            
                        # Found a valid word
                        if node.word:
                            res.add(node.word)

                        # Continue
                        visiting.add((r, c))
                        stack.append((r, c, node, True))
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = r + dr, c + dc
                            if nr in range(ROWS) and nc in range(COLS) and (nr, nc) not in visiting and board[nr][nc] in node.children:
                                stack.append((nr, nc, node.children[board[nr][nc]], False))
                            
        return list(res)
                