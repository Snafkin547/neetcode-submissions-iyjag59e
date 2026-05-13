class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        if len(matrix[0]) != n:
            return 
        matrix.reverse()
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
