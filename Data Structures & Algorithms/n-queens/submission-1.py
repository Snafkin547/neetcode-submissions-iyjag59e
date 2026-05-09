class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
       
        def stringify(arr):
            clean_arr = ["Q" if x == -1 else "." for x in arr]
            st_arr = []
            for i in range(0, n * n, n):
                st_arr.append("".join(clean_arr[i : i + n]))
            return st_arr

        ''' Mark impossible by vertical, horizontal, diagonal-left diagonal-right
            Next position checks:
                - left + horizontal: h
                - top + vertical: v
                - top_left + diagonal_left: l
                - top_right + diagonal_right: r
                - no constraint: empty
        '''
        
        def bt(i, k, curr):
            # Base Case
            if i == n * n:
                if not k:
                    res.append(stringify(curr))
                return
            
            # row, col: i//n, i%n
            row, col = i//n, i%n

            left = i - 1
            top = (i//n - 1)*n + i%n
            top_left = top - 1
            top_right = top + 1

            # TODO: Optimize with binary
            val = 0

            # Horizontal
            if col != 0 and (curr[left] == -1 or curr[left] & (1 << 1)):
                val |= (1 << 1)
            
            # Vertical
            if row != 0 and (curr[top] == -1 or curr[top] & (1 << 2)):
                val |= (1 << 2)
            
            # Diagonal left
            if row != 0 and col != 0 and (curr[top_left] == -1 or curr[top_left] & (1 << 3)):
                val |= (1 << 3)
            
            # Diagonal right
            if row != 0 and col != n - 1 and (curr[top_right] == -1 or curr[top_right] & (1 << 4)):
                val |= (1 << 4)
            
            curr.append(val)
            
            # With Q, if clear
            if curr[i] == 0:
                curr[i] = -1
                bt(i + 1, k - 1, curr)
                curr[i] = 0
            
            # Without Q
            bt(i + 1, k, curr)
            curr.pop()
            return

        bt(0, n, [])
        return res
