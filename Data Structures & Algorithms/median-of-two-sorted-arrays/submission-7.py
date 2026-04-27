class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def helper(arrA, lenA, arrB, lenB, k, startA = 0, startB = 0):
            if lenA > lenB:
                return helper(arrB, lenB, arrA, lenA, k, startB, startA)
            
            if lenA == 0:
                return arrB[startB + k - 1]

            if k == 1:
                return min(arrA[startA], arrB[startB])


            i = min(lenA, k//2)
            j = min(lenB, k//2)
            # Since we have k elements left to check, index k//2 - 1 is where we wanna see 
            if arrA[startA + i - 1] < arrB[startB + j -1]:
                return helper(arrA, lenA - i, arrB, lenB, k - i, startA + i, startB)
            else:
                return helper(arrA, lenA, arrB, lenB - j, k - j, startA, startB + j)
        
        left = (len(nums1) + len(nums2) + 1)//2
        right = (len(nums1) + len(nums2) + 2)//2

        return (helper(nums1, len(nums1), nums2, len(nums2), left) + helper(nums1, len(nums1), nums2, len(nums2),right))/2
