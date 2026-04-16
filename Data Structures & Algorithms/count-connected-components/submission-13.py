# DSU, if diff parent increment
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Maintain visited
        # for loop and traverse, appending to visited
        # A new node found in parent loop, then increment res

        mp = defaultdict(list)
        visited = set()
        res = 0
        for a, b in edges:
            mp[a].append(b)
            mp[b].append(a)

        for i in range(n):
            if i not in visited:
                res += 1
                visited.add(i)
                q = deque(mp[i])

                while q:
                    node = q.popleft()
                    if node not in visited:
                        visited.add(node)
                        for child in mp[node]:
                            if child not in visited:
                                q.append(child)

        return res
                