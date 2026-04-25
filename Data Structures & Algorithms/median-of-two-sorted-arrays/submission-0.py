class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = list(heapq.merge(nums1, nums2))
        if len(merged) %2 :
            return merged[len(merged)//2]
        else:
            return (merged[len(merged)//2 - 1] + merged[len(merged)//2])/2