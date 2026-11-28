"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        graph = {} # old:new, add node upon creation, managed visited state
        def dfs(curr):
            if not curr:
                return
            graph[curr] = Node(curr.val)
            new = graph[curr] # whats in st always exists
            for nei in curr.neighbors:
                # Create and Recurse
                if nei not in graph:
                    graph[nei] = Node(nei.val) 
                    dfs(nei)
                    
                # Connect
                new.neighbors.append(graph[nei])
        dfs(node)
        return graph[node] if node else None