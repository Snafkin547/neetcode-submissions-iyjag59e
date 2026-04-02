class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def explore(row, col, idx):
            # Successfully located the word
            if idx == len(word):
                return True

            # Out of bounds
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False

            # Already visited cell
            if board[row][col] == True:
                return False

            # Not matching
            if board[row][col] != word[idx]:
                return False

            # Marking the visit
            temp = board[row][col]
            board[row][col] = True

            # Continue Search
            found = explore(row + 1, col, idx+1) or explore(row - 1, col, idx+1) or explore(row, col + 1, idx+1) or explore(row, col - 1, idx+1)
            board[row][col] = temp
            return found

        for r in range(len(board)):
            for c in range(len(board[0])):
                if explore(r, c, 0):
                    return True
        return False 