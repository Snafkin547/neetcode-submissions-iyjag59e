class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        flag = False
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid

            # Logic for if left/right is sorted
            if nums[l] <= nums[mid]: # left is sorted
                if nums[l] <= target and target < nums[mid]:
                    r = mid -1 # cut off right
                else:
                    l = mid + 1 # cut off left

            else: # right is sorted
            # elif nums[mid] <= nums[r]: # right is sorted
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1 # cut off left
                else:
                    r = mid - 1
        return -1