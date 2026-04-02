class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) ==0 or target < nums[0] or nums[-1] < target:
            return -1
            
        l, r = 0, len(nums)
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1