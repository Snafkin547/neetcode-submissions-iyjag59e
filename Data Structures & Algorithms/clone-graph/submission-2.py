"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # initiate two queues one for original and the other for the copy
        # return the last elem
        if not node:
            return None
        
        q = deque([node])
        visited = {}
        visited[node] = Node(node.val)
        
        while q:
            o = q.popleft()
            for n in o.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val)
                    q.append(n)
                
                visited[o].neighbors.append(visited[n])
                    
        return visited[node]



