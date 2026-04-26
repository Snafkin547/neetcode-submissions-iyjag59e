class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        m, n = len(nums1), len(nums2)
        median1 = midian2 = float('-inf')
        while i + j < (m + n)//2 + 1:
            median2 = median1
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    median1 = nums1[i]
                    i += 1
                else:
                    median1 = nums2[j]
                    j += 1
            elif i < m:
                median1 = nums1[i]
                i += 1
            else:
                median1 = nums2[j]
                j += 1

        if (m + n) % 2:
            return float(median1)
        else:
            return (median1 + median2)/2.0
