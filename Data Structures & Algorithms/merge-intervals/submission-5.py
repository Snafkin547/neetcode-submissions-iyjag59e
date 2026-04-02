class Solution:
    def merge_sort(self, arr):
        def merge(left, right):
            i = j = 0
            res = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            res.extend(left[i:])
            res.extend(right[j:])
            return res


        if len(arr) <= 1:
            return arr
        i = len(arr) >> 1
        l = self.merge_sort(arr[:i])
        r = self.merge_sort(arr[i:])
        return merge(l, r)

        

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # Sort
        intervals = self.merge_sort(intervals)
        # Merge
        res = []
        curr = intervals[0]
        for i in range(1, len(intervals)):
            # If not overlapping
            if curr[1] < intervals[i][0]:
                res.append(curr)
                curr = intervals[i]
            # If overlapping
            else:
                curr = [
                    min(curr[0], intervals[i][0]),
                    max(curr[1], intervals[i][1])
                    ]
        res.append(curr)
        return res