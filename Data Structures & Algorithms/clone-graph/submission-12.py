"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 

        q = deque([node])
        graph = {} # old:new, add node upon creation
        graph[node] = Node(node.val) #managed visited state too

        while q:
            curr = q.popleft()
            new = graph[curr] # whats in st always exists
            for nei in curr.neighbors:
                # Push and create
                if nei not in graph:
                    q.append(nei)
                    graph[nei] = Node(nei.val) 
                    
                # Connect
                new.neighbors.append(graph[nei])
        return graph[node]