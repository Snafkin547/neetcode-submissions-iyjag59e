class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        if len(matrix[0]) != n:
            return 

        # Layer from 0 < (n + 1)//2
        for layer in range((n + 1)//2):
            # Pointer starts from layer < n - layer - 1 (last elem goes else where)
            for pointer in range(layer, n - layer - 1):
                
                TL = matrix[layer][pointer]
                
                # Top Left ([layer, pointer]) = Bottom Left ([n - pointer - 1, layer]
                matrix[layer][pointer] = matrix[n - pointer - 1][layer]
                # Bottom Left ([n - pointer - 1, layer] = Bottom Right ([n - layer - 1, n - pointer - 1])
                matrix[n - pointer - 1][layer] = matrix[n - layer - 1][n - pointer - 1]
                # Bottom Right ([n - layer - 1, n - pointer - 1]) = Top Right([pointer, n - layer - 1]
                matrix[n - layer - 1][n - pointer - 1] = matrix[pointer][n - layer - 1]
                # Top Right = Top Left
                matrix[pointer][n - layer - 1] = TL
