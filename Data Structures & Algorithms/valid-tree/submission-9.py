class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Cycle and isolated nodes lead to False
        # 1) Use DFS to detect cycle
        # 2) Check if the tree is len(visited) = n at the end
        if len(edges) != n -1:
            return False
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        stack = [0]
        visited = set([0])
        while stack:
            curr = stack.pop()
            for neighbor in tree[curr]:
                if neighbor not in visited:
                    visited.add(neighbor) # Mark immediately
                    stack.append(neighbor)
        return len(visited) == n
