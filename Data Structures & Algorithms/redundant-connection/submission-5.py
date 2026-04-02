class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        deg = [0] * (n + 1)
        nei = [[] for i in range(n + 1)]
        for a, b in edges:
            nei[a].append(b)
            nei[b].append(a)
            deg[a] += 1
            deg[b] += 1
        q = deque()
        for i in range(n + 1):
            if deg[i] == 1:
                q.append(i)
        
        while q:
            curr = q.popleft()
            deg[curr] -= 1
            for n in nei[curr]:
                deg[n] -= 1
                if deg[n] == 1:
                    q.append(n)
        
        for a, b in reversed(edges):
            if deg[a] == 2 and deg[b]:
                return [a, b]
        return []
            
