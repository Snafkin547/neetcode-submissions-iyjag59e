class Solution:
    def rob(self, nums: List[int]) -> int:
        # 5, 3, 1, 4
        # 5, 3, 1
        # 3, 1, 4
        '''
        Two passes without each end
        '''
        # Base Case
        if len(nums) == 1:
            return nums[0]
        # Pass One: Without last
        second, last = 0, 0
        for n in nums[:-1]:
            temp = max(second + n, last)
            second = last
            last = temp

        # Pass Two: Without first
        second2, last2 = 0, 0
        for n in nums[1:]:
            temp = max(second2 + n, last2)
            second2 = last2
            last2 = temp
        return max(last, last2)
