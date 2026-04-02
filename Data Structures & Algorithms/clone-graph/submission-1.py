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
        copy_node = Node(node.val)
        q = deque()
        q.append((node, copy_node))
        visited = {}
        
        while q:
            o, c = q.popleft()
            visited[c.val] = c
            for n in o.neighbors:
                cn = Node(n.val) if n.val not in visited else visited[n.val]
                c.neighbors.append(cn)
                if n.val not in visited:
                    q.append((n, cn))
                    
        return copy_node



