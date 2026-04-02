class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Use Remainig list and Curr list
        # append if remaining is empty
        res = []
        def dfs(curr, visited):
            if len(visited) == len(nums):
                res.append(curr.copy())
            
            for i in range(len(nums)):
                if i in visited:
                    continue
                curr.append(nums[i])
                visited.add(i)

                dfs(curr, visited)

                curr.pop()
                visited.remove(i)

        dfs([], set())
        return res