class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) < 1 or s[0] == '0':
            return 0

        res = 0
        # Keep adding valid
        def dfs(idx):
            
            nonlocal res
            
            if idx == len(s):
                res += 1
                return
            
            if s[idx] == '0':
                return

            # If one digits
            dfs(idx + 1)
            
            # If two digits
            if idx + 1 < len(s) and int(s[idx: idx + 2]) <= 26:
                print(s[idx: idx + 2])
                dfs(idx + 2)

        dfs(0)
        return res
        