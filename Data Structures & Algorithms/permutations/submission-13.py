class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = [False] * n
        # maintain ongoing 
        # mark visited in array or bit
        # for loop and visit unvisited
        def dfs(curr, visited):
            if len(curr) == n:
                res.append(curr[::])
                return
            
            for i in range(n):
                if visited[i]:
                    continue
                curr.append(nums[i])
                visited[i] = True
                dfs(curr, visited)
                visited[i] = False
                curr.pop()
                
        dfs([], visited)
        return res
