class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numMap = set(nums)
        longest = 0
        for n in nums:
            if not n - 1 in numMap:
                k = n
                count = 0
                while k in numMap:
                    k+=1
                    count += 1
                longest = max(longest, count)
        return longest 
        