class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for idx, n in enumerate(nums):
            if target - n in pos:
                return [pos[target-n], idx]
            else:
                pos[n] = idx


