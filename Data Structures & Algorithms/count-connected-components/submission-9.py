class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        count = 0
        for i in range(n):
            if i in visited:
                continue
            visited.add(i)
            count += 1
            stack = [i]
            while stack:
               curr = stack.pop()
               for node in graph[curr]:
                  if node not in visited:
                     visited.add(node)
                     stack.append(node)
        return count
