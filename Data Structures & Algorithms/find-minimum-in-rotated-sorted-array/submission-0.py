class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search + left and right if not tails
        l, r = 0, len(nums) - 1
        while l<=r:
            mid = (l + r) // 2
            # When should you say its here: if mid-1 is greater
            if mid != 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]

            # When should you check only left: if nums[-1] is greater
            elif nums[mid] < nums[-1]:
                r = mid - 1
            # When should you check only right: else
            else:
                l = mid + 1
        return nums[0]
