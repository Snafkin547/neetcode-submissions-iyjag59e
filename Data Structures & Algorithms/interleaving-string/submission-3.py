# State: i, j, k, isFirst, number of slices
# Ops: move i and/or j if either/both match with k-th char

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}
        def dfs(i, j, k, n1, n2):
            if k == len(s3):
                return abs(n1 + n2) <= 1

            if (i, j) in dp:
                return dp[(i, j)]

            # Exhausted one of strings
            if i == len(s1):
                return s2[j:] == s3[k:] and abs(n1 + n2 + 1) <= 1
            elif j == len(s2):
                return s1[i:] == s3[k:] and abs(n1 + n2 + 1) <= 1
                    

            # No match with curr s3: impossible
            if s1[i] != s3[k] and s2[j] != s3[k]:
                return False

            # Explore the remaining
            if n1 == 0 and n2 == 0:
                if s1[0] == s3[0] and dfs(1, 0, 1, -1, 0):
                    return True
                elif s2[0] == s3[0] and dfs(0, 1, 1, 0, -1):
                    return True
                else:
                    return False
            if n1 < 0:
                if s1[i] == s3[k] and dfs(i + 1, j, k + 1, n1, n2):
                    return True
                elif s2[j] == s3[k] and dfs(i, j + 1, k + 1, -n1, -n2 - 1):
                    return True
                else:
                    dp[(i, j)] = False
                    return False
            elif n2 < 0:
                if s1[i] == s3[k] and dfs(i + 1, j, k + 1, -n1 - 1, -n2):
                    return True
                elif s2[j] == s3[k] and dfs(i, j + 1, k + 1, n1, n2):
                    return True
                else:
                    dp[(i, j)] = False
                    return False
            return False
            
        return dfs(0, 0, 0, 0, 0)