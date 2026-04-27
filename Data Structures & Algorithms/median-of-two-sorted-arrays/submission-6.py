class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def helper(arrA, lenA, arrB, lenB, k, startA=0, startB=0):
            # Always ensure arrA is the shorter array
            if lenA > lenB:
                return helper(arrB, lenB, arrA, lenA, k, startB, startA)
            
            # Base cases
            if lenA == 0:
                return arrB[startB + k - 1]
            if k == 1:
                return min(arrA[startA], arrB[startB])

            # Divide k between the two arrays
            i = min(lenA, k // 2)
            j = k - i # Ensure i + j = k

            if arrA[startA + i - 1] < arrB[startB + j - 1]:
                # Discard the first i elements of arrA
                return helper(arrA, lenA - i, arrB, lenB, k - i, startA + i, startB)
            else:
                # Discard the first j elements of arrB
                return helper(arrA, lenA, arrB, lenB - j, k - j, startA, startB + j)
        
        total_len = len(nums1) + len(nums2)
        left = (total_len + 1) // 2
        right = (total_len + 2) // 2

        # Average of two middle elements handles both even and odd total lengths
        return (helper(nums1, len(nums1), nums2, len(nums2), left) + 
                helper(nums1, len(nums1), nums2, len(nums2), right)) / 2.0