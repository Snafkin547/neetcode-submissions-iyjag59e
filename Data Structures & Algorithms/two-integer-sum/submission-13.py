class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rec = {} # val, idx
        for i, n in enumerate(nums):
            if target - n in rec:
                return [rec[target - n], i]
            rec[n] = i
        return 
                