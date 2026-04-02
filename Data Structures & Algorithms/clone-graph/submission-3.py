"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(curr):
            if not curr:
                return None
        
            if curr not in visited:
                visited[curr] = Node(curr.val)
                for n in curr.neighbors:
                    visited[curr].neighbors.append(dfs(n))
            return visited[curr]
        return dfs(node)