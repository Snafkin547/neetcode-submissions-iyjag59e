class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numMap = defaultdict(int)
        longest = 0
        for n in nums:
            if not numMap[n]:
                numMap[n] = numMap[n - 1] + numMap[n + 1] + 1
                numMap[n - numMap[n - 1]] = numMap[n]
                numMap[n + numMap[n + 1]] = numMap[n]
                longest = max(longest, numMap[n])
        return longest
        