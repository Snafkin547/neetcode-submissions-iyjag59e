class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        if len(matrix[0]) != n:
            return 

        # Layer from 0 < (n + 1)//2
        for layer in range((n + 1)//2):
            # Pointer starts from layer < n - layer - 1 (last elem goes else where)
            for pointer in range(layer, n - layer - 1):
                # Top Left ([layer, pointer]) to Top Right([pointer, n - layer - 1])
                TR = matrix[pointer][n - layer - 1]
                matrix[pointer][n - layer - 1] = matrix[layer][pointer]
                # Top Right([pointer, n - layer - 1] to Bottom Right ([n - layer - 1, n - pointer - 1])
                BR = matrix[n - layer - 1][n - pointer - 1]
                matrix[n - layer - 1][n - pointer - 1] = TR
                # Bottom Right ([n - layer - 1, n - pointer - 1]) to Bottom Left ([n - pointer - 1, layer])
                BL = matrix[n - pointer - 1][layer]
                matrix[n - pointer - 1][layer] = BR
                # Bottom Left ([n - pointer - 1, layer]) to Top Left ([layer, pointer])
                matrix[layer][pointer] = BL
        