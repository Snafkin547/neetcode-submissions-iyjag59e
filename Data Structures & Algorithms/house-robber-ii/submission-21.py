class Solution:
    def rob(self, nums: List[int]) -> int:
        # State: How much so far
        # Ops: If this one + prev vs curr
        # Catch: if n <= 2: return max of nums
        n = len(nums)
        if n <= 2:
            return max(nums)

        def smart_robber(start, end):
            dp = [0] * (end - start)
            prev = nums[start]
            curr = max(nums[start], nums[start + 1])
            for i in range(start + 2, end):
                temp = max(curr, prev + nums[i])
                prev, curr = curr, temp
            return curr

        return max(smart_robber(0, n - 1), smart_robber(1, n))

