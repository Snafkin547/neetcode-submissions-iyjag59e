class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mp = defaultdict(list)    
        res = []

        for a, b in reversed(edges):
            mp[a].append(b)
            mp[b].append(a)

        for a, b in reversed(edges):

            stack = [(a, b)]
            visited = set()
            while stack:
                node, prev = stack.pop()
                
                if node == b:
                    return [a, b]
                elif node in visited:
                    break
                else:
                    visited.add(node)

                for d in mp[node]:
                    if d == prev:
                        continue
                    stack.append((d, node))
