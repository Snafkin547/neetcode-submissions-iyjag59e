class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = []
        backward = deque()
        res =[]
        curr = 1
        for i in range(len(nums)):
            curr *= nums[i]
            forward.append(curr)

        curr = 1
        for i in range(len(nums)-1, -1, -1):
            curr *= nums[i]
            # backward = [curr] + backward
            backward.appendleft(curr)

        for i in range(len(nums)):
            if i == 0:
                res.append(backward[1])
            elif i == len(nums) - 1:
                res.append(forward[i-1])
            else:
                res.append(forward[i-1] * backward[i+1])
        return res
