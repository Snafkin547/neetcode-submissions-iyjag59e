class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        i = 0
        n = len(nums)
        res = [[]]
        while i < n:
            # Treat same val as a group
            s = i
            while s < n and nums[i] == nums[s]:
                s += 1
            count = s - i
            
            # Append same val count times
            size = len(res)
            while count:
                for idx in range(size):
                    curr = res[idx].copy()
                    for c in range(count):
                        curr.append(nums[i])
                    res.append(curr)
                count -= 1
            i = s
        return res
