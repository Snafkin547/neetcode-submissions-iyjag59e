class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
       
        def stringify(arr):
            clean_arr = ["Q" if x == "Q" else "." for x in arr]
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
            val = ["_"] * 4

            # Horizontal
            if col != 0 and (curr[left] == 'Q' or curr[left][0] == 'h'):
                val[0] = 'h'
            
            # Vertical
            if row != 0 and (curr[top] == 'Q' or curr[top][1] == 'v'):
                val[1] = 'v'
            
            # Diagonal left
            if row != 0 and col != 0 and (curr[top_left]== 'Q' or curr[top_left][2] == 'l'):
                val[2] = 'l'
            
            # Diagonal right
            if row != 0 and col != n - 1 and (curr[top_right] == 'Q' or curr[top_right][3] == 'r'):
                val[3] = 'r'
            
            curr.append("".join(val))
            
            # With Q, if clear
            if curr[i] == '____':
                curr[i] = 'Q'
                bt(i + 1, k - 1, curr)
                curr[i] = '____'
            
            # Without Q
            bt(i + 1, k, curr)
            curr.pop()
            return

        bt(0, n, [])
        return res
