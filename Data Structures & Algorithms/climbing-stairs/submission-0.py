class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0]
        def helper(cur):
            if cur < 0:
                return
            elif cur == 0:
                res[0]+=1
            else:
                helper(cur-1)
                helper(cur-2)
        helper(n)
        return res[0]