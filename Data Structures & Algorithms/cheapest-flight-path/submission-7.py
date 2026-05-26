class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        mp = defaultdict(list) # from: cost, to
        for fm, to, cost in flights:
            if fm == dst:
                continue
            mp[fm].append((to, cost))

        visited = [float('inf')] * n # node: cost
        visited[src] = 0
        q = deque([(src, 0)]) # node, cost

        # bfs < k 
        steps = -1
        while steps < k and q:
            for _ in range(len(q)):
                node, ttl = q.popleft()                
                for nei, cost in mp[node]:
                    if ttl + cost < visited[nei]:
                        q.append((nei, ttl + cost))
                        visited[nei] = ttl + cost
            steps += 1
        return visited[dst] if visited[dst] != float('inf') else -1