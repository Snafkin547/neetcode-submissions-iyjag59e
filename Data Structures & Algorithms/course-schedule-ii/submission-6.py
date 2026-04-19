class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # keep track of whats been completed/visiting/unvisited
        # skip starting anything completed
        # detect cycle by visiting
        state =[0] * numCourses
        res = []
        mp = defaultdict(list)
        for a, b in prerequisites:
            mp[a].append(b)

        def dfs(node):
            nonlocal res
            if state[node] == 1:
                return True
            elif state[node] == -1:
                return False

            state[node] = -1
            for nei in mp[node]:
                if not dfs(nei):
                    return False
            state[node] = 1
            res.append(node)
            return True

        for task in range(numCourses):
            if not dfs(task):
                return []
        return res

