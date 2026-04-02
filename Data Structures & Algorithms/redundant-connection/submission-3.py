class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        nei = defaultdict(list)

        for a, b in edges:
            nei[a].append(b)
            nei[b].append(a)

        visited = [False] * (n + 1)
        cycle = set()
        cycleStart = -1

        def dfs(node, p):
            nonlocal cycleStart
            if visited[node]:
                cycleStart = node
                return True
            
            visited[node] = True
            for n in nei[node]:
                if n == p:
                    continue
                if dfs(n, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if cycleStart == node:
                        cycleStart = -1
                    return True
            return False
        dfs(1, -1)
        for a, b in reversed(edges):
            if a in cycle and b in cycle:
                return [a, b]
        return []
