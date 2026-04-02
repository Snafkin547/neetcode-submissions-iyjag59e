class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cnt = 0
        visited = set()
        nei = defaultdict(list)
        
        for a, b in edges:
            nei[a].append(b)
            nei[b].append(a)

        for num in range(n):
            if num in visited:
                continue
            s = [num]
            visiting = {num}
            while s:
                curr = s.pop()
                for n in nei[curr]:
                    if n not in visiting:
                        visiting.add(n)
                        visited.add(n)
                        s.append(n)
            cnt += 1
        return cnt