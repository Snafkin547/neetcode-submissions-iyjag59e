class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numset = set()
        for n in nums:
            if n in numset:
                return n
            numset.add(n)
                