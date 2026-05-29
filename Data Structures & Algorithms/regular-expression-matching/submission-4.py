class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        visited = {}

        def dfs(i, j):

            if (i, j) in visited:
                return visited[(i, j)]

            # pattern exhausted
            if j < 0:
                return i < 0

            # string exhausted
            if i < 0:
                # remaining pattern must be x*y*z*
                while j >= 1 and p[j] == '*':
                    j -= 2
                return j < 0
            visited[(i, j)] = False
            # normal character match
            if p[j] == s[i] or p[j] == '.':
                visited[(i, j)] = dfs(i - 1, j - 1)

            elif p[j] == '*':
                visited[(i, j)] |= dfs(i, j - 2) # Entirely skipping wild card
                if p[j - 1] == '.' or p[j - 1] == s[i]:
                    visited[(i, j)] |= dfs(i - 1, j) # j/* stays here while checking i forward

            return visited[(i, j)]
        return dfs(len(s)-1, len(p)-1)
