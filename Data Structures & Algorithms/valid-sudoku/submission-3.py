class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check duplicate using a set
        # Do row by row, col by col, box by box
        # Integrate them into a single loop
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                if v in rows[r] or v in cols[c] or v in box[(r//3, c//3)]:
                    return False
                rows[r].add(v)
                cols[c].add(v)
                box[(r//3, c//3)].add(v)
        return True


