class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Cycle and isolated nodes lead to False
        # 1) Use DFS to detect cycle
        # 2) Check if the tree is len(visited) = n at the end
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        stack = [(0, None)]
        visited = set()
        while stack:
            curr, prev = stack.pop()
            if curr in visited:
                print(curr, visited)
                return False
            visited.add(curr)
            for x in tree[curr]:
                if x != prev:
                    stack.append((x, curr))
        return len(visited) == n
