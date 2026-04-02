class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = set()
        for n in nums:
            mp.add(n)
        return len(mp) < len(nums)