class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def explore(row, col, visited, idx):
            # Successfully located the word
            if idx == len(word):
                return True

            # Out of bounds
            if row < 0 or row >= len(visited) or col < 0 or col >= len(visited[0]):
                return False

            # Already visited cell
            if visited[row][col]:
                return False

            # Not matching
            if board[row][col] != word[idx]:
                return False

            # Marking the visit
            visited[row][col] = True
            print(f'{idx}: {board[row][col]}')
            print(visited)

            # Continue Search
            found = explore(row + 1, col, visited, idx+1) or explore(row - 1, col, visited, idx+1) or explore(row, col + 1, visited, idx+1) or explore(row, col - 1, visited, idx+1)
            visited[row][col] = False
            return found

        for r in range(len(board)):
            for c in range(len(board[0])):
                matrix = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
                if explore(r, c, matrix, 0):
                    return True
        return False 