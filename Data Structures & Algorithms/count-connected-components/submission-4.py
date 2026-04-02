class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cnt = 0
        visited = [False] * n
        nei = [[] for _ in range(n)]
        
        for a, b in edges:
            nei[a].append(b)
            nei[b].append(a)

        for num in range(n):
            if visited[num]:
                continue
            q = deque([num])
            while q:
                curr = q.popleft()
                for n in nei[curr]:
                    if not visited[n]:
                        visited[n] = True
                        q.append(n)
            cnt += 1
        return cnt