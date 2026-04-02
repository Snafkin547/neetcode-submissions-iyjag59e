class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        indegree = [0] * (len(edges) + 1)
        graph = defaultdict(list)
        for a, b in edges:
            indegree[a] += 1
            indegree[b] += 1
            graph[a].append(b)
            graph[b].append(a)

        q = deque()
        for i in range(1, len(edges) + 1):
            if indegree[i] == 1:
                q.append(i)
        
        while q:
            curr = q.popleft()
            indegree[curr] -= 1
            for nei in graph[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)
        for a, b in reversed(edges):
            if indegree[a] > 1 and indegree[b] > 1:
                return[a, b]
        return []
            