class Solution:
    def rob(self, nums: List[int]) -> int:
        ''' Keep track of last and second, 
            so every decision is last vs second + curr        
        '''
        second, last = 0, 0
        for n in nums:
            temp = max(second+n, last)
            second = last
            last = temp
        return last
