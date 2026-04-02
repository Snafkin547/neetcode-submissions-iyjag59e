class BisecLeft:
    def __init__(self):
        self.arr = []
    
    def find(self, elm):
        l, r = 0, len(self.arr)
        while l < r:
            m = l + ((r - l) >> 1)
            if elm <= self.arr[m]:
                r = m
            else:
                l = m + 1
        return l

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        bt = BisecLeft()
        res = 0
        for i in range(len(nums)):
            idx = bt.find(nums[i])
            if idx == len(bt.arr):
                bt.arr.append(nums[i])
                res += 1
            else:
                bt.arr[idx] = nums[i]
        return res