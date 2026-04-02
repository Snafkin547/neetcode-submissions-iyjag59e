class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Sliding Window
        '''
        Split the nums into zero-free arrays
        Time: O(n)
        Memory: O(n)
        '''
        arr = []
        curr = []
        for n in nums:
            if n == 0:
                arr.append(curr)
                curr = []
            else:
                curr.append(n)
        if curr:
            arr.append(curr)
        
        res = max(nums)
        # Count negs and process differently
        for a in arr:
            negs = 0
            for n in a:
                if n < 0:
                    negs += 1
            
            # Even
            if negs%2 == 0:
                prod = 1
                for n in a:
                    prod *= n
                    res = max(res, prod)
            
            # Odd
            else:
                prod = 1
                for n in a:
                    prod *= n
                    res = max(res, prod)
                prod = 1
                for n in reversed(a):
                    prod *= n
                    res = max(res, prod)
        return res

                

