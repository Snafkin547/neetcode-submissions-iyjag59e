"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        rel_map = {}

        def dfs(curr):
            if curr in rel_map:
                return rel_map[curr]

            rel_map[curr] = Node(curr.val)
            for nei in curr.neighbors:
                rel_map[curr].neighbors.append(dfs(nei))
            return rel_map[curr]

        return dfs(node) if node else None