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
            return None

        q = deque([node])
        rel_map = {node:Node(node.val)}

        while q:
            curr = q.popleft()
            for nei in curr.neighbors:
                if nei not in rel_map:
                    rel_map[nei] = Node(nei.val)
                    q.append(nei)
                rel_map[curr].neighbors.append(rel_map[nei])

        return rel_map[node]