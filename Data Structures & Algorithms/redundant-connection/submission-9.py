class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Build a graph
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # Check if two nodes are cycled
        def connected(curr, prev, target, visited):
            if curr == target:
                return True
            visited.add(curr)
            for nei in graph[curr]:
                if nei == prev or nei in visited:
                    continue
                if connected(nei, curr, target, visited):
                    return True
            return False

        # Traverse from end to beginning
        for a, b in reversed(edges):
            if connected(b, a, a, set()):
                return [a, b]
        return []

        # Clarify no self reference and repeated edges