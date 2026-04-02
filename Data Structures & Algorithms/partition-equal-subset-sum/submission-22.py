class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        res = sum(nums)
        if res != (res >> 1) << 1:
            return False
        res >>= 1
        dp = set()
        dp.add(0)
        for i in range(len(nums) - 1, -1, -1):
            nextdp = set()
            for t in dp:
                if t + nums[i] == res:
                    return True
                nextdp.add(t + nums[i])
                nextdp.add(t)
            dp = nextdp
        return False