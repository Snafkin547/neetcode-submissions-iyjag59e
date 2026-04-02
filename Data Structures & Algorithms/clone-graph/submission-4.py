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
        stack = [node]
        visited = {}
        visited[node] = Node(node.val)
        while stack:
           curr = stack.pop()
           for n in curr.neighbors:
               if n not in visited:
                  visited[n] = Node(n.val)
                  visited[curr].neighbors.append(visited[n])
                  stack.append(n)
               else:
                  visited[curr].neighbors.append(visited[n])
        return visited[node]