class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Use Remainig list and Curr list
        # append if remaining is empty
        res = []
        def dfs(curr, balance):
            if not balance:
                res.append(curr.copy())
            
            n = len(balance)
            for i in range(n):
                val = balance.popleft()
                curr.append(val)
                dfs(curr, balance)
                curr.pop()
                balance.append(val)
        q = deque(nums)
        dfs([], q)
        return res