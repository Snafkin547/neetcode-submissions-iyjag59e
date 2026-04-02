class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Edge case: duplicated numbers result in same perm
        nums.sort()
        def dfs(curr, balance):
            if not balance:
                res.append(curr.copy())
                return
            for i in range(len(balance)):
                if i > 0 and balance[i] == balance[i - 1]:
                    continue
                curr.append(balance[i])
                dfs(curr, balance[:i] + balance[i+1:])
                curr.pop()
        dfs([], nums)
        return res