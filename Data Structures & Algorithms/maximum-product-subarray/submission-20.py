class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def helper(start, end, isEven):

            if start + 1 == end:
                return nums[start]

            if start >= len(nums) or end <= 0:
                return -11

            # Even # of negs
            if isEven:
                res = nums[start]
                for i in range(start+1, end):
                    res *= nums[i]
                return res

            # Odd # of negs
            else:
                # Look up first neg
                f = start
                while nums[f] > 0:
                    f += 1
                pre = helper(0, f, True)
                noFirst = helper(f + 1, end, True)

                # Look up last neg
                l = end - 1
                while nums[l] > 0:
                    l -= 1
                appen = helper(l + 1, end, True)
                noLast = helper(start, l, True)
                return max(max(pre, noFirst), max(appen, noLast))
                

        # Split array between zeros
        # Count negs: Address cases Odd/Even
        start = 0
        negs = 0
        res = -11
        for idx, n in enumerate(nums):
            if n == 0:
                res = max(0, max(res, helper(start, idx, negs%2==0)))
                start = idx + 1
                negs = 0
            if n < 0:
                negs += 1
        res = max(res, helper(start, idx + 1, negs%2==0))
        return res
