class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        steps = [len(matrix[0]), len(matrix) -1] # col/row boundary
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # row/col dir
        res = []
        r, c, d = 0, -1, 0 # d makes the system behave differently odd/even = row/col move
        while steps[d & 1]:
            for i in range(steps[d & 1]):
                r += directions[d][0]
                c += directions[d][1]
                res.append(matrix[r][c])
            steps[d & 1] -= 1
            d += 1
            d %= 4
        return res