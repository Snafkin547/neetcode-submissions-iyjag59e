class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        zeRow = zeroCOL = False

        # Check first row and col
        for r in range(ROWS):
            if matrix[r][0] == 0:
                zeRow = True
                break
        for c in range(COLS):
            if matrix[0][c] == 0:
                zeroCOL = True
                break

        # taint headers to be zero
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = matrix[r][0] = 0
        
        # flip all rows and cols with a '0' taint
        for r in range(1, ROWS):
            if matrix[r][0] == 0:
                for c in range(1, COLS):
                    matrix[r][c] = 0

        for c in range(1, COLS):
            if matrix[0][c] == 0:
                for r in range(1, ROWS):
                    matrix[r][c] = 0

        # Flip first row and col if appropriate
        if zeRow:
            for r in range(ROWS):
                matrix[r][0] = 0
        if zeroCOL:
            for c in range(COLS):
                matrix[0][c] = 0
            