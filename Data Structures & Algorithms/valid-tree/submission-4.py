class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # No cycle : track state
        # No isolated branch/nodes : reachable from a single node
        # Check if all nodes were visited in the traversal
        if n <= 1 and not edges:
            return True
        states = [1] * n
        nei= defaultdict(list)
        node = edges[0][0]
        for p, s in edges:
            nei[p].append(s)
            nei[s].append(p)
        
        q = deque([(node, None)])
        while q:
            curr, prev = q.popleft()
            if states[curr] == 0:
                return False
            states[curr] = 0
            for b in nei[curr]:
                if b != prev:
                   q.append((b, curr))
        return sum(states) == 0

