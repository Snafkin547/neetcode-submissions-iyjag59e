class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # memorize
        numSet = {}
        for idx, n in enumerate(nums):
            if target - n in numSet:
                smaller = numSet[target - n] if numSet[target - n] <= idx else idx
                bigger = numSet[target - n] if numSet[target - n] > idx else idx
                return [smaller, bigger]
            else:
                numSet[n] = idx
        return []
