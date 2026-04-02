class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Lookup possible row
        ## first elem < target
        # Look up within the row

        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (r+l)//2
            row = matrix[mid]
            if target < row[0]:
                r = mid - 1
            elif row[0] < target:
                l = mid +1
            else:
                break
        thisRow = matrix[(r+l)//2]
        l, r = 0, len(thisRow)-1
        while l <= r:
            mid = (l+r)//2
            if thisRow[mid] == target:
                return True
            elif target < thisRow[mid]:
                r= mid -1
            else:
                l = mid + 1
        return False  



