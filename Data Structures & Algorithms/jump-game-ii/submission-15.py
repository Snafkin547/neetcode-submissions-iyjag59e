class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        l = r = 0
        while r < len(nums) - 1:
            reach = 0
            for i in range(l, r + 1):
                reach = max(reach, i + nums[i])
            l = r + 1
            r = reach
            count += 1
        return count
