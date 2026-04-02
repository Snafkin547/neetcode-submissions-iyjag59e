class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row wise
        for arr in board:
            numSet = set()
            for elm in arr:
                if elm in numSet:
                    return False
                if elm != '.':
                    numSet.add(elm)
        # col wise
        for col in range(len(board)):
            numSet = set()
            for row in range(len(board)):
                elm = board[row][col]
                if elm in numSet:
                    return False
                if elm != '.':
                    numSet.add(elm)

        # box wise
        one = two = three = None
        for idx, arr in enumerate(board):
            numSet = None
            if idx%3 == 0:
                one, two, three = set(), set(), set()
            for col, elm in enumerate(arr):
                if col < 3:
                    numSet = one
                elif col < 6:
                    numSet = two
                else:
                    numSet = three

                if elm in numSet:
                    return False
                if elm != '.':
                    numSet.add(elm)
        return True



