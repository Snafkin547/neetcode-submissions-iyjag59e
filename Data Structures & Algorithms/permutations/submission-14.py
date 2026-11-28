class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = 0
        # maintain ongoing 
        # mark visited in array or bit
        # for loop and visit unvisited
        def dfs(curr, visited):
            if len(curr) == n:
                res.append(curr[::])
                return
            
            for i in range(n):
                if visited & (1 << i):
                    continue
                curr.append(nums[i])
                visited |= (1 << i)
                dfs(curr, visited)
                visited ^= (1 << i)
                curr.pop()

        dfs([], visited)
        return res
