class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        mp = defaultdict(list) # from: cost, to
        for fm, to, cost in flights:
            if fm == dst:
                continue
            mp[fm].append((to, cost))

        visited = [float('inf')] * n # node: cost
        q = deque([(src, 0)]) # node, cost

        # bfs < k 
        steps = -1
        while steps <= k and q:
            for i in range(len(q)):
                node, ttl = q.popleft()
                if ttl > visited[node]:
                    continue
                visited[node] = ttl
                for nei, cost in mp[node]:
                    if ttl + cost < visited[nei]:
                        q.append((nei, ttl + cost))
            steps += 1
        return visited[dst] if visited[dst] != float('inf') else -1