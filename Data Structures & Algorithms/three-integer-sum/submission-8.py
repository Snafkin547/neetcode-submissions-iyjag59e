class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        # pick a pivot
        # left = pivot + 1, right = n-1
        # append all till left == right but move till diff
        pivot = 0
        res =[]
        while pivot < n - 2:
            if nums[pivot] > 0:
                break

            l, r = pivot + 1, n - 1
            while l < r:
                curr = nums[pivot] + nums[l] + nums[r]
                if curr == 0:
                    res.append([nums[pivot], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                    r -= 1
                    while l < r and nums[r + 1] == nums[r]:
                        r -= 1
                elif curr < 0:
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                       l += 1
                else:
                    r -= 1
                    while l < r and nums[r + 1] == nums[r]:
                        r -= 1

            pivot += 1
            while  pivot < n - 1 and nums[pivot-1]== nums[pivot]:
                pivot += 1
        return res