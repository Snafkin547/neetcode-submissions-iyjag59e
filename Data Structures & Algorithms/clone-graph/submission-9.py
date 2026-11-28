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

        st = [node]
        visited = set([node]) # mark visited upon push(avd:inf loop)
        
        graph = defaultdict(Node) # old:new, add node upon creation
        graph[node] = Node(node.val) 

        while st:
            curr = st.pop()
            new = graph[curr] # whats in st always exists
            for nei in curr.neighbors:
                # Push and create
                if nei not in visited:
                    visited.add(nei)
                    st.append(nei)
                    graph[nei] = Node(nei.val) 
                    
                # Connect
                new.neighbors.append(graph[nei])
        return graph[node]