class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res =[[] for _ in range(n+1)]
        res[0] = ['']

        for k in range(n+1):
            for i in range(k):
                for l in res[i]:
                    for r in res[k-i-1]:
                        res[k].append('('+l+')'+r)
        return res[-1]
        