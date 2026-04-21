class Solution:
    def trap(self, height: List[int]) -> int:
        # Two pointers
        n = len(height)
        l = res = curr = block = 0
        r = 1
        while l < n and r < n:
            h = min(height[l], height[r])
            w = r - l - 1
            curr = max(curr, h * w - block)
            
            # Reset pointers and block count
            if height[l] <= height[r]:
                l = r
                r += 1
                res += curr
                curr = block = 0

            # Anything lower will be considered block
            else:
                block += height[r]
                r += 1
        res += curr

        l = n - 1
        r = l - 1
        res2 = curr = block = 0
        while l >= 0 and r >= 0:
            h = min(height[l], height[r])
            w = l - r - 1
            curr = max(curr, h * w - block)
            
            # Reset pointers and block count
            if height[l] <= height[r]:
                l = r
                r -= 1
                res2 += curr
                curr = block = 0

            # Anything lower will be considered block
            else:
                block += height[r]
                r -= 1

        res2 += curr
        return max(res, res2)
