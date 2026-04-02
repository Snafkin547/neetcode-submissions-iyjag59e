class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Go left and right each, and store so far val
        f_curr = b_curr = 1
        forward = []
        backward = []
        n = len(nums)

        for i in range(n):
            forward.append(f_curr)
            backward.append(b_curr)
            f_curr *= nums[i]
            b_curr *= nums[n - i - 1]
        
        res = []
        for i in range(n):
            res.append(forward[i] * backward[n - i - 1])
        return res

        
            