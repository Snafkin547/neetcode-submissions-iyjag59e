class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def helper(idx, arr):
            if idx == n:
                res.append(arr[::])
                return
            
            for i in range(idx, n):
                arr[idx], arr[i] = arr[i], arr[idx]
                helper(idx + 1, arr)
                arr[idx], arr[i] = arr[i], arr[idx]
        helper(0, nums)
        return res