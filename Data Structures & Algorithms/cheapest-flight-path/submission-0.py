class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        mp = defaultdict(list) # from: cost, to
        for fm, to, cost in flights:
            if fm == dst:
                continue
            mp[fm].append((to, cost))

        visited = {} # node: cost
        q = deque([(src, 0)]) # node, cost

        # bfs < k 
        steps = -1
        while steps <= k and q:
            for i in range(len(q)):
                node, ttl = q.popleft()
                visited[node] = min(visited[node], ttl) if node in visited else ttl
                for nei, cost in mp[node]:
                    if nei not in visited or ttl + cost < visited[nei]:
                        q.append((nei, ttl + cost))
                
            steps += 1
        return visited[dst] if dst in visited else -1