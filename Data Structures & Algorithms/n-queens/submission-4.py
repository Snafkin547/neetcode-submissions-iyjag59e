class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        curr = [0] * (n * n)
        
        def stringify(arr):
            clean_arr = ["Q" if x == -1 else "." for x in arr]
            st_arr = []
            for i in range(0, n * n, n):
                st_arr.append("".join(clean_arr[i : i + n]))
            return st_arr
        
        def bt(row, k):
            # Base Case
            if row == n:
                if not k:
                    res.append(stringify(curr))
                return
            elif row + k > n:
                return

            # Precompute inherited vals from a row above
            for col in range(n):
                i = row * n + col
                left = i - 1
                top = (i//n - 1)*n + i%n
                top_left = top - 1
                top_right = top + 1

                mask = 0 # Horizontal: No need as always alone
              
                # Vertical
                if row != 0 and (curr[top] == -1 or curr[top] & (1 << 2)):
                    mask |= (1 << 2)
                
                # Diagonal left
                if row != 0 and col != 0 and (curr[top_left] == -1 or curr[top_left] & (1 << 3)):
                    mask |= (1 << 3)
                
                # Diagonal right
                if row != 0 and col != n - 1 and (curr[top_right] == -1 or curr[top_right] & (1 << 4)):
                    mask |= (1 << 4)
                
                curr[i] = mask
            
            # Recurse Down
            for col in range(n):
                i = row * n + col    
                # With Q, if clear
                if curr[i] == 0:
                    curr[i] = -1
                    bt(row + 1, k - 1)
                    curr[i] = 0
                
                # Without Q
                bt(row + 1, k)
            return

        bt(0, n)
        return res
