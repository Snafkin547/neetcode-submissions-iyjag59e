class Solution:
    def rob(self, nums: List[int]) -> int:
        ''' Keep track of last and second, 
            so every decision is last vs second + curr        
        '''
        last = nums[0]
        for i in range(1, len(nums)):

            curr = nums[i]

            if i == 1:
                nums[i] = max(last, curr)                
            else:
                nums[i] = max(last, second+curr)

            second = last
            last = nums[i]            
        
        return nums[-1]