class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # No cycle : track state
        # No isolated branch/nodes : reachable from a single node
        # Check if all nodes were visited in the traversal
        if n - 1!= len(edges):
            return False
        
        nei= defaultdict(list)
        
        for p, s in edges:
            nei[p].append(s)
            nei[s].append(p)
        
        q = deque([0])
        visited = {0}
        while q:
            curr = q.popleft()
            for b in nei[curr]:
                if b not in visited:
                   q.append(b)
                   visited.add(b)
        return len(visited) == n

