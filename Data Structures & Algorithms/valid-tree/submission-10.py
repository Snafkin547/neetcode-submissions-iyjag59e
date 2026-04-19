class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        # No cycle, No isolated trees/reachable from any tree
        mp = defaultdict(list)
        for a, b in edges:
            mp[a].append(b)
            mp[b].append(a)
        
        stack = [(0, -1)]
        visited = set()
        while stack:
            curr, prev = stack.pop()
            visited.add(curr)
            for nei in mp[curr]:
                if nei == prev:
                    continue
                if nei in visited:
                    return False
                stack.append((nei, curr))
        return len(visited) == n