class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for idx, n in enumerate(nums):
            if target - n in mp:
                return [mp[target - n], idx]
            mp[n] = idx
        return -1