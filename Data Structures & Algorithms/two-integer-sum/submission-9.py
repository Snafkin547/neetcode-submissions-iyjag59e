class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for idx, n in enumerate(nums):
            if target - n in prev:
                return [prev[target-n], idx]
            prev[n] = idx
        return None