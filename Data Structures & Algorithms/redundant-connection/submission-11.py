class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Build a graph
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # Check if two nodes are cycled
        cycled = set()
        visited = [False] * (len(edges) + 1)
        cycle_start = -1
        def connected(curr, prev):
            nonlocal cycle_start
            if visited[curr]:
                cycle_start = curr
                return True

            visited[curr] = True
            for nei in graph[curr]:
                if nei == prev:
                    continue
                if connected(nei, curr):
                    if cycle_start != -1:
                        cycled.add(curr)
                    if curr == cycle_start:
                        cycle_start = -1
                    return True
            return False
        
        connected(1, 0)
        print(cycled)
        # Traverse from end to beginning
        for a, b in reversed(edges):
            if a in cycled and b in cycled:
                return [a, b]
        return []

        # Clarify no self reference and repeated edges