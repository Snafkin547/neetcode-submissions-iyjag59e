class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = set()
        for n in nums:
            if n in mp:
                return True
            mp.add(n)
        return False