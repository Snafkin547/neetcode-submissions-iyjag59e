class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
    
        nei = defaultdict(list)
        def dfs(node, p):
            if visited[node]:
                return True
            visited[node] = True
            for nb in nei[node]:
                if nb != p:
                    if dfs(nb, node):
                        return True
            return False
        
        for a, b in edges:
            visited = [False] * (n + 1)
            nei[a].append(b)
            nei[b].append(a)
            if dfs(a, -1):
                return [a, b]
        return []