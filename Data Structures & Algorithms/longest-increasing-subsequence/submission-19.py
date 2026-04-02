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
        if l == len(self.arr):
            self.arr.append(elm)
        else:
            self.arr[l] = elm
        return len(self.arr)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # In bisec Tree, find left most index at the moment
        # The number of elem to the right + itself is the increasing subsequence
        bt = BisecLeft()
        for n in nums:
            bt.find(n)
        return len(bt.arr)

            