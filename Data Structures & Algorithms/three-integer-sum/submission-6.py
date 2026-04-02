class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            small, big = i + 1, len(nums) - 1

            while small < big:
                threeSum = nums[i] + nums[small] + nums[big]
                if threeSum > 0:
                    big -= 1
                elif threeSum < 0:
                    small += 1
                else:
                    res.append([nums[i], nums[small], nums[big]])
                    small += 1
                    big -= 1
                    while nums[small] == nums[small - 1] and small < big:
                        small += 1
        return res