class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # State: i, j
        # Ops: increment and move one & move both if same
        m, n = len(word1), len(word2)
        dp = {}
        def helper(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i

            if (i, j) in dp:
                return dp[(i, j)]

            if word1[i] != word2[j]:
                dp[(i, j)] = 1 + min(helper(i + 1, j), helper(i, j + 1), helper(i + 1, j + 1))
            else:
                dp[(i, j)] = helper(i + 1, j + 1)
            return dp[(i, j)]
        return helper(0, 0)