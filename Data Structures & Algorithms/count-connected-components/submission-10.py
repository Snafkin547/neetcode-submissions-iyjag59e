class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [0] * n
        count = 0
        for i in range(n):
            if visited[i]:
                continue
            visited[i] = 1
            count += 1
            stack = [i]
            while stack:
               curr = stack.pop()
               for node in graph[curr]:
                  if not visited[node]:
                     visited[node]=1
                     stack.append(node)
        return count
