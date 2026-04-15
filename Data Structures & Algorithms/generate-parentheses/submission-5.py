class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [[""]]
        for i in range(n):
            size = len(res)
            curr = []
            for j in range(size):
                left = res[j]
                right = res[size - 1 - j]
                for l in left:
                    for r in right:
                        curr.append(l + "(" + r + ")")
            res.append(curr)
        return res[-1]

