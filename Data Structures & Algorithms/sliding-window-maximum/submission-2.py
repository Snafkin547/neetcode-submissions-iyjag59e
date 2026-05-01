class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        leftMax = [0] * n
        leftMax[0] = nums[0]
        rightMax = [0] * n
        rightMax[n - 1] = nums[n - 1]
        
        for i in range(1, n):
            if i % k == 0:
                leftMax[i] = nums[i]
            else:
                leftMax[i] = max(leftMax[i - 1], nums[i])
            if (n - i - 1) % k == 0:
                rightMax[n - i - 1] = nums[n - i - 1]
            else:
                rightMax[n - i - 1] = max(rightMax[n - i], nums[n - i - 1])
        res = []
        for i in range(n - k + 1):
            res.append(max(leftMax[i + k - 1], rightMax[i]))
        return res