class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        ttl = len(nums1) + len(nums2)
        half = ttl//2

        if len(A) > len(B):
            A, B = B, A
        l, r = 0, len(A) - 1
        while True:
            i = l + (r - l) //2
            j = half - i - 2
            
            # This ensures following comparison always valid in edge cases
            Aleft = A[i] if i >= 0 else float('-inf') # Edge Case: A doesnt belong to left
            Aright = A[i + 1] if i + 1 < len(A) else float('inf') # Edge Case: A is empty
            Bleft = B[j] if j >= 0 else float('-inf') # Edge Case: B is empty
            Bright = B[j + 1] if j + 1< len(B) else float('inf')# Edge Case: B doesnt belong to left

            if Aleft <= Bright and Bleft <= Aright:
                if ttl%2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright))/2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
