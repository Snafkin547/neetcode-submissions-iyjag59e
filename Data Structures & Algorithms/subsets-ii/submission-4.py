class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        def bt(idx, curr):
            res.append(curr.copy())
            
            for i in range(idx, n):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                bt(i + 1, curr)
                curr.pop()

        bt(0, [])
        return res